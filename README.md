# Django 참조
본 레포지토리는 Django 참조 관계에 대한 이해를 돕기 위해 만들어진 레포지토리입니다.
정참조, 역참조, `select_related()`, `prefetch_related()` 에 관한 내용입니다.

더 자세한 내용은 해당 기술 블로그를 확인해주세요. ( [Django 참조](https://velog.io/@dev_taehyun/Django-%EC%A0%95%EC%B0%B8%EC%A1%B0%EC%99%80-%EC%97%AD%EC%B0%B8%EC%A1%B0) )

1. `reference.sql` 파일을 통해 SQL 데이터를 저장하여 사용하면 됩니다.
2. `reference` 디렉토리 내에 있는 `settings.py` 파일 속 아래 코드를 통해 Django ORM 활용에 따른 SQL Query 및 디버깅을 확인할 수 있습니다.

    ```python
    LOGGING = {
        'disable_existing_loggers': False,
        'version': 1,
        'formatters': {
            'verbose': {
                'format': '{asctime} {levelname} {message}',
                'style': '{'
            },
        },
        'handlers': {
            'console': {
                'class'     : 'logging.StreamHandler',
                'formatter' : 'verbose',
                'level'     : 'DEBUG',
            },
            'file': {
                'level'     : 'DEBUG',
                'class'     : 'logging.FileHandler',
                'formatter' : 'verbose',
                'filename'  : 'debug.log',
            },
        },
        'loggers': {
            'django.db.backends': {
                'handlers' : ['console','file'],
                'level'    : 'DEBUG',
                'propagate': False,
            },
        },
    }
    ```
3. Migration 관련하여 문제가 발생할 경우 `reference_test` > `migrations` 디렉토리 내에 있는 `0001_initial.py`을 삭제한 이후 다시 `python manage.py makemigrations reference_test`와 `python manage.py migrate`을 진행해주세요.

