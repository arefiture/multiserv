# Важно при старте ECA:

1. Создать директорию `key/` на уровне файла `manage.py`
2. Перейти в эту директорию через `cd key/`
3. Создать ключи для данного проекта:
```sh
openssl genrsa -out eca_private.pem 2048
openssl rsa -in eca_private.pem -pubout -out eca_public.pem
```
4. Передать ключ `eca_public.pem` другим проектам, где будет использоваться ЕСА.
> ***ВАЖНО***: `eca_private.pem` никому не передавать!