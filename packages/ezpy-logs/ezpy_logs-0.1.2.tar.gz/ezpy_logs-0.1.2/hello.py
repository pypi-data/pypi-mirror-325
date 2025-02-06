from ezpy_logs.LoggerFactory import LoggerFactory

LoggerFactory.setup_LoggerFactory(log_dir=".logs")
logger = LoggerFactory.getLogger(__name__)

def main():
    logger.info("Hello from ezpy-logs!")

if __name__ == "__main__":
    main()
