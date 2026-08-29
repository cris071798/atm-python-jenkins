FROM atm-python-base:1.0
WORKDIR /app
COPY atm.py .
COPY test_atm.py .
CMD ["python", "atm.py"]
