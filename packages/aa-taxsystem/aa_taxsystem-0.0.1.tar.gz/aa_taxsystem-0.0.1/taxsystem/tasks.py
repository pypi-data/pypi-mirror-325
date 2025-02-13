"""App Tasks"""

from celery import shared_task

from allianceauth.services.tasks import QueueOnce

from taxsystem.decorators import when_esi_is_available
from taxsystem.hooks import get_extension_logger
from taxsystem.models.tax import OwnerAudit
from taxsystem.task_helpers.general_helpers import enqueue_next_task, no_fail_chain
from taxsystem.task_helpers.wallet_helpers import update_corp_wallet_division

logger = get_extension_logger(__name__)


@shared_task
@when_esi_is_available
def update_all_corps(runs: int = 0):
    corps = OwnerAudit.objects.select_related("corporation").all()
    for corp in corps:
        update_corp.apply_async(args=[corp.corporation.corporation_id])
        runs = runs + 1
    logger.info("Queued %s Corp Audit Updates", runs)


@shared_task(bind=True, base=QueueOnce)
def update_corp(self, corp_id, force_refresh=False):  # pylint: disable=unused-argument
    corp = OwnerAudit.objects.get(corporation__corporation_id=corp_id)
    logger.debug("Processing Audit Updates for %s", corp.corporation.corporation_name)
    que = []

    que.append(update_corp_wallet.si(corp_id, force_refresh=force_refresh))

    enqueue_next_task(que)

    logger.debug("Queued Audit Updates for %s", corp.corporation.corporation_name)


@shared_task(
    bind=True,
    base=QueueOnce,
    once={"graceful": False, "keys": ["corp_id"]},
    name="taxsystem.tasks.update_corp_wallet",
)
@no_fail_chain
def update_corp_wallet(
    self, corp_id, force_refresh=False, chain=[]
):  # pylint: disable=unused-argument, dangerous-default-value
    return update_corp_wallet_division(corp_id, force_refresh=force_refresh)
