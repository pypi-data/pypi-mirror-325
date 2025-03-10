from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from . import tasks
from .models import Activity, Collection, Domain, Message, Object
from .signals import activity_received


@receiver(post_save, sender=Message)
def on_message_created_process(sender, **kw):
    message = kw["instance"]

    if kw["created"]:
        tasks.process_message.delay_on_commit(str(message.id))


@receiver(post_save, sender=Domain)
def on_domain_created_fetch_nodeinfo(sender, **kw):
    domain = kw["instance"]

    if kw["created"]:
        tasks.fetch_nodeinfo.delay(domain_name=domain.name)


@receiver(pre_save, sender=Activity)
@receiver(pre_save, sender=Object)
def on_ap_object_create_define_related_collections(sender, **kw):
    instance = kw["instance"]
    reference = instance.reference

    if reference is None:
        return

    match (instance.type, instance.replies):
        case (Activity.Types.QUESTION | Object.Types.NOTE, None):
            instance.replies = reference.domain.build_collection(
                name=f"Replies to {reference.uri}",
                ordering_method=Collection.OrderingMethods.NONE,
            )
        case _:
            pass


@receiver(activity_received, sender=Activity)
def on_activity_received_process_standard_flows(sender, **kw):
    activity = kw["activity"]

    tasks.process_standard_activity_flows(activity_uri=activity.uri)
