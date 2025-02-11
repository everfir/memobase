FROM neo-dev-cn-beijing.cr.volces.com/common/python:3.11-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN python3.11 -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --no-cache-dir

COPY ./memobase_server /app/memobase_server
COPY ./api.py /app
COPY ./config.yaml /app

# 创建并写入.env文件
RUN echo "DATABASE_URL=postgresql://pgsql:DevEverfir07@postgres-85cf826906e9-public.rds-pg.volces.com:5432/memobase" > /app/.env && \
    echo "REDIS_URL=redis://default:EverFir%23NeoRedisprod2024..@redis-cnlflentbp4diuf8a.redis.volces.com:6379" >> /app/.env && \
    echo "ACCESS_TOKEN=secret" >> /app/.env

CMD ["python3.11", "-m", "fastapi", "run", "api.py"]
