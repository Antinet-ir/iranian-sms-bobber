from concurrent.futures import ThreadPoolExecutor
from time import sleep
from core.logger import Logger

def send_request(service_name, module, phone, logger, dry_run=False):
    try:
        if dry_run:
            print(f"[DRY-RUN] {service_name} -> {phone}")
            logger.log(service_name, phone, "N/A", "dry-run")
            return

        response = module.send(phone)
        status = response.status_code
        if 200 <= status < 300:
            print(f"[OK] {service_name} -> {status}")
            logger.log(service_name, phone, status, "success")
        else:
            print(f"[FAIL] {service_name} -> {status}")
            logger.log(service_name, phone, status, "fail")
    except Exception as e:
        print(f"[ERROR] {service_name} -> {str(e)}")
        logger.log(service_name, phone, "ERROR", "exception", str(e))

def run_campaign(phone, services_dict, rounds, max_threads, delay, logger: Logger, dry_run=False):
    for r in range(rounds):
        print(f"\n[ROUND {r+1}/{rounds}] Starting...")
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            for name, module in services_dict.items():
                executor.submit(send_request, name, module, phone, logger, dry_run)
        if r + 1 < rounds:
            sleep(delay)
    logger.save()
