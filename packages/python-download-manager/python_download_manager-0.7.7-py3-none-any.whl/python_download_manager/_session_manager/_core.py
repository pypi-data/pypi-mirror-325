from requests import Session


class SessionManager:
    __session: Session = None

    @classmethod
    def initialize(cls, headers: dict = None, proxies: dict = None):
        cls.__session = Session()
        cls.__session.headers.update(headers or {})
        cls.__session.proxies.update(proxies or {})

    @classmethod
    def close(cls):
        if cls.__session is not None:
            cls.__session.close()
            cls.__session = None

    @classmethod
    def get(cls, url: str, headers=None, proxies=None, stream=True, **kwargs):
        return cls.__session.get(
            url, headers=headers, proxies=proxies, stream=stream, **kwargs
        )

    @classmethod
    def head(cls, url: str, headers=None, proxies=None, **kwargs):
        return cls.__session.head(
            url, headers=headers, proxies=proxies, allow_redirects=True, **kwargs
        )
