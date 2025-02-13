from typing import Optional, Callable, Any
import os
import redis
import pickle

from utils_hj3415 import setup_logger
mylogger = setup_logger(__name__,'INFO')


def connect_to_redis(addr: str, password: str) -> redis.Redis:
    conn_str = f"Connect to Redis ..."
    mylogger.info(conn_str, f"Server Addr : {addr}")
    # decode_responses=False 로 설정해서 바이트 반환시켜 피클을 사용할 수 있도록한다.
    return redis.StrictRedis(host=addr, port=6379, db=0, decode_responses=False, password=password)

def select_redis_addr() -> str:
    mode = os.getenv("DB_MODE", 'LOCAL')
    if mode == 'DEV':
        redis_addr = os.getenv('DEV_REDIS', '')
    elif mode == 'LOCAL':
        redis_addr = os.getenv('LOCAL_REDIS', 'redis://localhost:6379/')
    elif mode == 'DOCKER':
        redis_addr = os.getenv('DOCKER_REDIS', 'redis://redis:6379/')
    else:
        raise Exception("Invalid value in MODE env variable.")
    return redis_addr


class Base:
    """
    Redis 캐싱을 위한 기본 클래스
    """
    redis_client = connect_to_redis(addr=select_redis_addr(), password=os.getenv('REDIS_PASSWORD', ''))

    # 기본 Redis 캐시 만료 시간 (1일)
    DEFAULT_CACHE_EXPIRATION_SEC = 3600 * 24

    def __init__(self):
        """
        Base 클래스의 인스턴스를 초기화합니다.
        Redis 클라이언트가 정상적으로 초기화되지 않았다면 예외를 발생시킵니다.
        """
        if Base.redis_client is None:
            raise ValueError("myredis.Base.redis_client has not been initialized!")

    @classmethod
    def exists(cls, key_name: str) -> bool:
        """
        주어진 키가 Redis에 존재하는지 확인합니다.

        :param key_name: 확인할 Redis 키 이름
        :return: 키가 존재하면 True, 그렇지 않으면 False
        """
        if cls.redis_client.exists(key_name):
            return True
        else:
            return False

    @classmethod
    def get_ttl(cls, redis_name: str) -> Optional[int]:
        """
        Redis에서 특정 키의 TTL(남은 유효 시간)을 가져옵니다.

        :param redis_name: TTL을 확인할 Redis 키 이름
        :return: TTL 값(초 단위), 키가 없거나 TTL이 없을 경우 None
        """
        ttl = cls.redis_client.ttl(redis_name)

        if ttl == -1:
            mylogger.warning(f"{redis_name}는 만료 시간이 설정되어 있지 않습니다.")
            return None
        elif ttl == -2:
            mylogger.warning(f"{redis_name}는 Redis에 존재하지 않습니다.")
            return None
        else:
            mylogger.debug(f"{redis_name}의 남은 시간은 {ttl}초입니다.")
            return ttl


    @classmethod
    def delete(cls, redis_name: str):
        """
        Redis에서 특정 키를 삭제합니다. 키가 존재하지 않아도 오류 없이 진행됩니다.

        :param redis_name: 삭제할 Redis 키 이름
        """
        mylogger.debug(Base.list_redis_names())
        cls.redis_client.delete(redis_name)
        mylogger.debug(Base.list_redis_names())

    @classmethod
    def delete_all_with_pattern(cls, pattern: str):
        """
        주어진 패턴과 일치하는 모든 Redis 키를 삭제합니다.

        :param pattern: 삭제할 키의 패턴 (예: 'prefix*'는 prefix로 시작하는 모든 키를 삭제)
        """
        # print(Redis.list_redis_names())
        # SCAN 명령어를 사용하여 패턴에 맞는 키를 찾고 삭제
        cursor = '0'
        while cursor != 0:
            cursor, keys = cls.redis_client.scan(cursor=cursor, match=pattern, count=1000)
            if keys:
                cls.redis_client.delete(*keys)

        mylogger.debug(Base.list_redis_names())


    @classmethod
    def list_redis_names(cls, filter:str="all") -> list:
        """
        Redis에서 특정 필터와 일치하는 키 목록을 반환합니다.

        :param filter: 검색할 키의 필터. 기본값은 "all" (모든 키 반환)
        :return: 필터에 맞는 Redis 키 목록 (정렬됨)
        """
        # SCAN 명령어 파라미터
        pattern = b"*" if filter == "all" else f"*{filter}*".encode('utf-8')  # 부분 일치: *filter*
        mylogger.debug(f"pattern : {pattern}")
        cursor = "0"
        matched_keys = []

        while True:
            # SCAN 호출
            cursor, keys = cls.redis_client.scan(cursor=cursor, match=pattern, count=1000)
            mylogger.debug(f"cursor : {cursor}/{type(cursor)}")
            matched_keys.extend(keys)
            # 커서가 '0'이면 스캔이 끝났다는 의미
            if str(cursor) == "0":
                break

        return sorted(matched_keys)

    @classmethod
    def set_value(cls, redis_name: str, value: Any, expiration_sec: int = DEFAULT_CACHE_EXPIRATION_SEC) -> None:
        """
        Redis에 데이터를 저장합니다.

        :param redis_name: 저장할 Redis 키 이름
        :param value: 저장할 데이터 (pickle을 사용하여 직렬화)
        :param expiration_sec: 데이터의 만료 시간 (기본값: 1일)
        """
        cls.redis_client.setex(redis_name, expiration_sec, pickle.dumps(value))
        mylogger.info(f"Redis 캐시에 저장 (만료시간: {expiration_sec}초) - redis_name : {redis_name}")


    @classmethod
    def get_value(cls, redis_name: str) -> Any:
        """
        Redis에서 데이터를 가져옵니다.

        :param redis_name: 가져올 Redis 키 이름
        :return: 저장된 데이터 (pickle을 사용하여 역직렬화)
        """
        stored_data = cls.redis_client.get(redis_name)  # 키 "my_key"의 값을 가져옴
        value = pickle.loads(stored_data) if stored_data is not None else None # type: ignore
        return value


    @classmethod
    def fetch_and_cache_data(cls, redis_name: str, refresh: bool, fetch_function: Callable, *args, timer=DEFAULT_CACHE_EXPIRATION_SEC) -> Any:
        """
        Redis에서 캐시된 데이터를 가져오거나, 존재하지 않으면 제공된 함수를 실행하여 데이터를 가져온 후 캐시에 저장합니다.

        :param redis_name: Redis에 저장할 키 이름
        :param refresh: True이면 캐시를 강제로 갱신
        :param fetch_function: 데이터를 가져오는 함수
        :param timer: 캐시 만료 시간 (초 단위, 기본값: 1일)
        :param args: fetch_function에 전달할 추가 인자
        :return: 가져온 데이터 (pickle을 사용하여 역직렬화 가능)
        """
        if not refresh:
            value = cls.get_value(redis_name)
            ttl_hours = round(cls.redis_client.ttl(redis_name) / timer, 1)
            mylogger.info(f"Redis 캐시에서 데이터 가져오기 (남은시간: {ttl_hours} 시간) - redis_name : {redis_name}")
            if value:
                return value

        # 캐시된 데이터가 없거나 refresh=True인 경우
        value = fetch_function(*args)

        if value:
            cls.set_value(redis_name=redis_name, value=value, expiration_sec=timer)
        return value
