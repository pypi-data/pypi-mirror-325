r'''
# `cloudflare_notification_policy`

Refer to the Terraform Registry for docs: [`cloudflare_notification_policy`](https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy).
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class NotificationPolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicy",
):
    '''Represents a {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy cloudflare_notification_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        alert_type: builtins.str,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        email_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyEmailIntegration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        filters: typing.Optional[typing.Union["NotificationPolicyFilters", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        pagerduty_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPagerdutyIntegration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        webhooks_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyWebhooksIntegration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy cloudflare_notification_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#account_id NotificationPolicy#account_id}
        :param alert_type: The event type that will trigger the dispatch of a notification. See the developer documentation for descriptions of `available alert types <https://developers.cloudflare.com/fundamentals/notifications/notification-available/>`_. Available values: ``advanced_http_alert_error``, ``access_custom_certificate_expiration_type``, ``advanced_ddos_attack_l4_alert``, ``advanced_ddos_attack_l7_alert``, ``bgp_hijack_notification``, ``billing_usage_alert``, ``block_notification_block_removed``, ``block_notification_new_block``, ``block_notification_review_rejected``, ``brand_protection_alert``, ``brand_protection_digest``, ``clickhouse_alert_fw_anomaly``, ``clickhouse_alert_fw_ent_anomaly``, ``custom_ssl_certificate_event_type``, ``dedicated_ssl_certificate_event_type``, ``dos_attack_l4``, ``dos_attack_l7``, ``expiring_service_token_alert``, ``failing_logpush_job_disabled_alert``, ``fbm_auto_advertisement``, ``fbm_dosd_attack``, ``fbm_volumetric_attack``, ``health_check_status_notification``, ``hostname_aop_custom_certificate_expiration_type``, ``http_alert_edge_error``, ``http_alert_origin_error``, ``image_notification``, ``image_resizing_notification``, ``incident_alert``, ``load_balancing_health_alert``, ``load_balancing_pool_enablement_alert``, ``logo_match_alert``, ``magic_tunnel_health_check_event``, ``maintenance_event_notification``, ``mtls_certificate_store_certificate_expiration_type``, ``pages_event_alert``, ``radar_notification``, ``real_origin_monitoring``, ``scriptmonitor_alert_new_code_change_detections``, ``scriptmonitor_alert_new_hosts``, ``scriptmonitor_alert_new_malicious_hosts``, ``scriptmonitor_alert_new_malicious_scripts``, ``scriptmonitor_alert_new_malicious_url``, ``scriptmonitor_alert_new_max_length_resource_url``, ``scriptmonitor_alert_new_resources``, ``secondary_dns_all_primaries_failing``, ``secondary_dns_primaries_failing``, ``secondary_dns_zone_successfully_updated``, ``secondary_dns_zone_validation_warning``, ``sentinel_alert``, ``stream_live_notifications``, ``traffic_anomalies_alert``, ``tunnel_health_event``, ``tunnel_update_event``, ``universal_ssl_event_type``, ``web_analytics_metrics_update``, ``weekly_account_overview``, ``workers_alert``, ``zone_aop_custom_certificate_expiration_type``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#alert_type NotificationPolicy#alert_type}
        :param enabled: The status of the notification policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#enabled NotificationPolicy#enabled}
        :param name: The name of the notification policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#name NotificationPolicy#name}
        :param description: Description of the notification policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#description NotificationPolicy#description}
        :param email_integration: email_integration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#email_integration NotificationPolicy#email_integration}
        :param filters: filters block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#filters NotificationPolicy#filters}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pagerduty_integration: pagerduty_integration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#pagerduty_integration NotificationPolicy#pagerduty_integration}
        :param webhooks_integration: webhooks_integration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#webhooks_integration NotificationPolicy#webhooks_integration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d26986a49b23bd0b8c252e62235f69de0aed407a858eb18dec93b2afb89ac0f4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NotificationPolicyConfig(
            account_id=account_id,
            alert_type=alert_type,
            enabled=enabled,
            name=name,
            description=description,
            email_integration=email_integration,
            filters=filters,
            id=id,
            pagerduty_integration=pagerduty_integration,
            webhooks_integration=webhooks_integration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a NotificationPolicy resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the NotificationPolicy to import.
        :param import_from_id: The id of the existing NotificationPolicy that should be imported. Refer to the {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the NotificationPolicy to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__125b1431b5b31917f637f01b7497a9caaaa8b98ffa586ee484008a61b146f960)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putEmailIntegration")
    def put_email_integration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyEmailIntegration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2609648347639c71060c162127a890fa79f5aa754008f528fe5bd16e169c51c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEmailIntegration", [value]))

    @jsii.member(jsii_name="putFilters")
    def put_filters(
        self,
        *,
        actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        affected_components: typing.Optional[typing.Sequence[builtins.str]] = None,
        airport_code: typing.Optional[typing.Sequence[builtins.str]] = None,
        alert_trigger_preferences: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Sequence[builtins.str]] = None,
        event: typing.Optional[typing.Sequence[builtins.str]] = None,
        event_source: typing.Optional[typing.Sequence[builtins.str]] = None,
        event_type: typing.Optional[typing.Sequence[builtins.str]] = None,
        group_by: typing.Optional[typing.Sequence[builtins.str]] = None,
        health_check_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        incident_impact: typing.Optional[typing.Sequence[builtins.str]] = None,
        input_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        limit: typing.Optional[typing.Sequence[builtins.str]] = None,
        megabits_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
        new_health: typing.Optional[typing.Sequence[builtins.str]] = None,
        new_status: typing.Optional[typing.Sequence[builtins.str]] = None,
        packets_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
        pool_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        product: typing.Optional[typing.Sequence[builtins.str]] = None,
        project_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        protocol: typing.Optional[typing.Sequence[builtins.str]] = None,
        requests_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
        selectors: typing.Optional[typing.Sequence[builtins.str]] = None,
        services: typing.Optional[typing.Sequence[builtins.str]] = None,
        slo: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_hostname: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_ip: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_zone_name: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel_name: typing.Optional[typing.Sequence[builtins.str]] = None,
        where: typing.Optional[typing.Sequence[builtins.str]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param actions: Targeted actions for alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#actions NotificationPolicy#actions}
        :param affected_components: Affected components for alert. Available values: ``API``, ``API Shield``, ``Access``, ``Always Online``, ``Analytics``, ``Apps Marketplace``, ``Argo Smart Routing``, ``Audit Logs``, ``Authoritative DNS``, ``Billing``, ``Bot Management``, ``Bring Your Own IP (BYOIP)``, ``Browser Isolation``, ``CDN Cache Purge``, ``CDN/Cache``, ``Cache Reserve``, ``Challenge Platform``, ``Cloud Access Security Broker (CASB)``, ``Community Site``, ``D1``, ``DNS Root Servers``, ``DNS Updates``, ``Dashboard``, ``Data Loss Prevention (DLP)``, ``Developer's Site``, ``Digital Experience Monitoring (DEX)``, ``Distributed Web Gateway``, ``Durable Objects``, ``Email Routing``, ``Ethereum Gateway``, ``Firewall``, ``Gateway``, ``Geo-Key Manager``, ``Image Resizing``, ``Images``, ``Infrastructure``, ``Lists``, ``Load Balancing and Monitoring``, ``Logs``, ``Magic Firewall``, ``Magic Transit``, ``Magic WAN``, ``Magic WAN Connector``, ``Marketing Site``, ``Mirage``, ``Network``, ``Notifications``, ``Observatory``, ``Page Shield``, ``Pages``, ``R2``, ``Radar``, ``Randomness Beacon``, ``Recursive DNS``, ``Registrar``, ``Registration Data Access Protocol (RDAP)``, ``SSL Certificate Provisioning``, ``SSL for SaaS Provisioning``, ``Security Center``, ``Snippets``, ``Spectrum``, ``Speed Optimizations``, ``Stream``, ``Support Site``, ``Time Services``, ``Trace``, ``Tunnel``, ``Turnstile``, ``WARP``, ``Waiting Room``, ``Web Analytics``, ``Workers``, ``Workers KV``, ``Workers Preview``, ``Zaraz``, ``Zero Trust``, ``Zero Trust Dashboard``, ``Zone Versioning``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#affected_components NotificationPolicy#affected_components}
        :param airport_code: Filter on Points of Presence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#airport_code NotificationPolicy#airport_code}
        :param alert_trigger_preferences: Alert trigger preferences. Example: ``slo``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#alert_trigger_preferences NotificationPolicy#alert_trigger_preferences}
        :param enabled: State of the pool to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#enabled NotificationPolicy#enabled}
        :param environment: Environment of pages. Available values: ``ENVIRONMENT_PREVIEW``, ``ENVIRONMENT_PRODUCTION``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#environment NotificationPolicy#environment}
        :param event: Pages event to alert. Available values: ``EVENT_DEPLOYMENT_STARTED``, ``EVENT_DEPLOYMENT_FAILED``, ``EVENT_DEPLOYMENT_SUCCESS``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#event NotificationPolicy#event}
        :param event_source: Source configuration to alert on for pool or origin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#event_source NotificationPolicy#event_source}
        :param event_type: Stream event type to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#event_type NotificationPolicy#event_type}
        :param group_by: Alert grouping. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#group_by NotificationPolicy#group_by}
        :param health_check_id: Identifier health check. Required when using ``filters.0.status``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#health_check_id NotificationPolicy#health_check_id}
        :param incident_impact: The incident impact level that will trigger the dispatch of a notification. Available values: ``INCIDENT_IMPACT_NONE``, ``INCIDENT_IMPACT_MINOR``, ``INCIDENT_IMPACT_MAJOR``, ``INCIDENT_IMPACT_CRITICAL``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#incident_impact NotificationPolicy#incident_impact}
        :param input_id: Stream input id to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#input_id NotificationPolicy#input_id}
        :param limit: A numerical limit. Example: ``100``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#limit NotificationPolicy#limit}
        :param megabits_per_second: Megabits per second threshold for dos alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#megabits_per_second NotificationPolicy#megabits_per_second}
        :param new_health: Health status to alert on for pool or origin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#new_health NotificationPolicy#new_health}
        :param new_status: Tunnel health status to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#new_status NotificationPolicy#new_status}
        :param packets_per_second: Packets per second threshold for dos alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#packets_per_second NotificationPolicy#packets_per_second}
        :param pool_id: Load balancer pool identifier. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#pool_id NotificationPolicy#pool_id}
        :param product: Product name. Available values: ``worker_requests``, ``worker_durable_objects_requests``, ``worker_durable_objects_duration``, ``worker_durable_objects_data_transfer``, ``worker_durable_objects_stored_data``, ``worker_durable_objects_storage_deletes``, ``worker_durable_objects_storage_writes``, ``worker_durable_objects_storage_reads``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#product NotificationPolicy#product}
        :param project_id: Identifier of pages project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#project_id NotificationPolicy#project_id}
        :param protocol: Protocol to alert on for dos. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#protocol NotificationPolicy#protocol}
        :param requests_per_second: Requests per second threshold for dos alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#requests_per_second NotificationPolicy#requests_per_second}
        :param selectors: Selectors for alert. Valid options depend on the alert type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#selectors NotificationPolicy#selectors}
        :param services: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#services NotificationPolicy#services}.
        :param slo: A numerical limit. Example: ``99.9``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#slo NotificationPolicy#slo}
        :param status: Status to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#status NotificationPolicy#status}
        :param target_hostname: Target host to alert on for dos. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#target_hostname NotificationPolicy#target_hostname}
        :param target_ip: Target ip to alert on for dos in CIDR notation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#target_ip NotificationPolicy#target_ip}
        :param target_zone_name: Target domain to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#target_zone_name NotificationPolicy#target_zone_name}
        :param tunnel_id: Tunnel IDs to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#tunnel_id NotificationPolicy#tunnel_id}
        :param tunnel_name: Tunnel Names to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#tunnel_name NotificationPolicy#tunnel_name}
        :param where: Filter for alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#where NotificationPolicy#where}
        :param zones: A list of zone identifiers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#zones NotificationPolicy#zones}
        '''
        value = NotificationPolicyFilters(
            actions=actions,
            affected_components=affected_components,
            airport_code=airport_code,
            alert_trigger_preferences=alert_trigger_preferences,
            enabled=enabled,
            environment=environment,
            event=event,
            event_source=event_source,
            event_type=event_type,
            group_by=group_by,
            health_check_id=health_check_id,
            incident_impact=incident_impact,
            input_id=input_id,
            limit=limit,
            megabits_per_second=megabits_per_second,
            new_health=new_health,
            new_status=new_status,
            packets_per_second=packets_per_second,
            pool_id=pool_id,
            product=product,
            project_id=project_id,
            protocol=protocol,
            requests_per_second=requests_per_second,
            selectors=selectors,
            services=services,
            slo=slo,
            status=status,
            target_hostname=target_hostname,
            target_ip=target_ip,
            target_zone_name=target_zone_name,
            tunnel_id=tunnel_id,
            tunnel_name=tunnel_name,
            where=where,
            zones=zones,
        )

        return typing.cast(None, jsii.invoke(self, "putFilters", [value]))

    @jsii.member(jsii_name="putPagerdutyIntegration")
    def put_pagerduty_integration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPagerdutyIntegration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e6d605bc183299465ed36999e058ed339c1c1d9d4260aabb5d8121c2decd657)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPagerdutyIntegration", [value]))

    @jsii.member(jsii_name="putWebhooksIntegration")
    def put_webhooks_integration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyWebhooksIntegration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcdb11383bda2c3b10780c02c32f0e2dfdfb687da0c11a00120f0b6ad6661f78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWebhooksIntegration", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEmailIntegration")
    def reset_email_integration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailIntegration", []))

    @jsii.member(jsii_name="resetFilters")
    def reset_filters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilters", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPagerdutyIntegration")
    def reset_pagerduty_integration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPagerdutyIntegration", []))

    @jsii.member(jsii_name="resetWebhooksIntegration")
    def reset_webhooks_integration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhooksIntegration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="created")
    def created(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "created"))

    @builtins.property
    @jsii.member(jsii_name="emailIntegration")
    def email_integration(self) -> "NotificationPolicyEmailIntegrationList":
        return typing.cast("NotificationPolicyEmailIntegrationList", jsii.get(self, "emailIntegration"))

    @builtins.property
    @jsii.member(jsii_name="filters")
    def filters(self) -> "NotificationPolicyFiltersOutputReference":
        return typing.cast("NotificationPolicyFiltersOutputReference", jsii.get(self, "filters"))

    @builtins.property
    @jsii.member(jsii_name="modified")
    def modified(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modified"))

    @builtins.property
    @jsii.member(jsii_name="pagerdutyIntegration")
    def pagerduty_integration(self) -> "NotificationPolicyPagerdutyIntegrationList":
        return typing.cast("NotificationPolicyPagerdutyIntegrationList", jsii.get(self, "pagerdutyIntegration"))

    @builtins.property
    @jsii.member(jsii_name="webhooksIntegration")
    def webhooks_integration(self) -> "NotificationPolicyWebhooksIntegrationList":
        return typing.cast("NotificationPolicyWebhooksIntegrationList", jsii.get(self, "webhooksIntegration"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="alertTypeInput")
    def alert_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="emailIntegrationInput")
    def email_integration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyEmailIntegration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyEmailIntegration"]]], jsii.get(self, "emailIntegrationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filtersInput")
    def filters_input(self) -> typing.Optional["NotificationPolicyFilters"]:
        return typing.cast(typing.Optional["NotificationPolicyFilters"], jsii.get(self, "filtersInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pagerdutyIntegrationInput")
    def pagerduty_integration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPagerdutyIntegration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPagerdutyIntegration"]]], jsii.get(self, "pagerdutyIntegrationInput"))

    @builtins.property
    @jsii.member(jsii_name="webhooksIntegrationInput")
    def webhooks_integration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyWebhooksIntegration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyWebhooksIntegration"]]], jsii.get(self, "webhooksIntegrationInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d61495632773ce0d55188dd5c264531790da548ad26191efd65e253d9ad7eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="alertType")
    def alert_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alertType"))

    @alert_type.setter
    def alert_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6c59bc8c4d370898c433afe11d54353dbb01e0117c5e68b0ebcca68e7bcdf69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df1ca562165db15d390fd123cc403797076f4dd2d4772623a50ab8a708b70143)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b59f2fa90359289bd4f53cbe0d77c9cf06b5a6eee45e84f5d1ad1ad9d7481c80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46a33d76b4aab3bd5c657ec06950c493c424c61455616973e446696aa8e28398)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c32685b847789725af6a3b296bc5149261a762977bb9e1060f4aedc88b42c842)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "alert_type": "alertType",
        "enabled": "enabled",
        "name": "name",
        "description": "description",
        "email_integration": "emailIntegration",
        "filters": "filters",
        "id": "id",
        "pagerduty_integration": "pagerdutyIntegration",
        "webhooks_integration": "webhooksIntegration",
    },
)
class NotificationPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        account_id: builtins.str,
        alert_type: builtins.str,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        email_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyEmailIntegration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        filters: typing.Optional[typing.Union["NotificationPolicyFilters", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        pagerduty_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPagerdutyIntegration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        webhooks_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyWebhooksIntegration", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#account_id NotificationPolicy#account_id}
        :param alert_type: The event type that will trigger the dispatch of a notification. See the developer documentation for descriptions of `available alert types <https://developers.cloudflare.com/fundamentals/notifications/notification-available/>`_. Available values: ``advanced_http_alert_error``, ``access_custom_certificate_expiration_type``, ``advanced_ddos_attack_l4_alert``, ``advanced_ddos_attack_l7_alert``, ``bgp_hijack_notification``, ``billing_usage_alert``, ``block_notification_block_removed``, ``block_notification_new_block``, ``block_notification_review_rejected``, ``brand_protection_alert``, ``brand_protection_digest``, ``clickhouse_alert_fw_anomaly``, ``clickhouse_alert_fw_ent_anomaly``, ``custom_ssl_certificate_event_type``, ``dedicated_ssl_certificate_event_type``, ``dos_attack_l4``, ``dos_attack_l7``, ``expiring_service_token_alert``, ``failing_logpush_job_disabled_alert``, ``fbm_auto_advertisement``, ``fbm_dosd_attack``, ``fbm_volumetric_attack``, ``health_check_status_notification``, ``hostname_aop_custom_certificate_expiration_type``, ``http_alert_edge_error``, ``http_alert_origin_error``, ``image_notification``, ``image_resizing_notification``, ``incident_alert``, ``load_balancing_health_alert``, ``load_balancing_pool_enablement_alert``, ``logo_match_alert``, ``magic_tunnel_health_check_event``, ``maintenance_event_notification``, ``mtls_certificate_store_certificate_expiration_type``, ``pages_event_alert``, ``radar_notification``, ``real_origin_monitoring``, ``scriptmonitor_alert_new_code_change_detections``, ``scriptmonitor_alert_new_hosts``, ``scriptmonitor_alert_new_malicious_hosts``, ``scriptmonitor_alert_new_malicious_scripts``, ``scriptmonitor_alert_new_malicious_url``, ``scriptmonitor_alert_new_max_length_resource_url``, ``scriptmonitor_alert_new_resources``, ``secondary_dns_all_primaries_failing``, ``secondary_dns_primaries_failing``, ``secondary_dns_zone_successfully_updated``, ``secondary_dns_zone_validation_warning``, ``sentinel_alert``, ``stream_live_notifications``, ``traffic_anomalies_alert``, ``tunnel_health_event``, ``tunnel_update_event``, ``universal_ssl_event_type``, ``web_analytics_metrics_update``, ``weekly_account_overview``, ``workers_alert``, ``zone_aop_custom_certificate_expiration_type``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#alert_type NotificationPolicy#alert_type}
        :param enabled: The status of the notification policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#enabled NotificationPolicy#enabled}
        :param name: The name of the notification policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#name NotificationPolicy#name}
        :param description: Description of the notification policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#description NotificationPolicy#description}
        :param email_integration: email_integration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#email_integration NotificationPolicy#email_integration}
        :param filters: filters block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#filters NotificationPolicy#filters}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pagerduty_integration: pagerduty_integration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#pagerduty_integration NotificationPolicy#pagerduty_integration}
        :param webhooks_integration: webhooks_integration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#webhooks_integration NotificationPolicy#webhooks_integration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(filters, dict):
            filters = NotificationPolicyFilters(**filters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bfdad0ea3b671f6ddd7c3f93399e6b1e1dbbec330f6748078f80895b3d1a900)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument alert_type", value=alert_type, expected_type=type_hints["alert_type"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument email_integration", value=email_integration, expected_type=type_hints["email_integration"])
            check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pagerduty_integration", value=pagerduty_integration, expected_type=type_hints["pagerduty_integration"])
            check_type(argname="argument webhooks_integration", value=webhooks_integration, expected_type=type_hints["webhooks_integration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "alert_type": alert_type,
            "enabled": enabled,
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if description is not None:
            self._values["description"] = description
        if email_integration is not None:
            self._values["email_integration"] = email_integration
        if filters is not None:
            self._values["filters"] = filters
        if id is not None:
            self._values["id"] = id
        if pagerduty_integration is not None:
            self._values["pagerduty_integration"] = pagerduty_integration
        if webhooks_integration is not None:
            self._values["webhooks_integration"] = webhooks_integration

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The account identifier to target for the resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#account_id NotificationPolicy#account_id}
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert_type(self) -> builtins.str:
        '''The event type that will trigger the dispatch of a notification.

        See the developer documentation for descriptions of `available alert types <https://developers.cloudflare.com/fundamentals/notifications/notification-available/>`_. Available values: ``advanced_http_alert_error``, ``access_custom_certificate_expiration_type``, ``advanced_ddos_attack_l4_alert``, ``advanced_ddos_attack_l7_alert``, ``bgp_hijack_notification``, ``billing_usage_alert``, ``block_notification_block_removed``, ``block_notification_new_block``, ``block_notification_review_rejected``, ``brand_protection_alert``, ``brand_protection_digest``, ``clickhouse_alert_fw_anomaly``, ``clickhouse_alert_fw_ent_anomaly``, ``custom_ssl_certificate_event_type``, ``dedicated_ssl_certificate_event_type``, ``dos_attack_l4``, ``dos_attack_l7``, ``expiring_service_token_alert``, ``failing_logpush_job_disabled_alert``, ``fbm_auto_advertisement``, ``fbm_dosd_attack``, ``fbm_volumetric_attack``, ``health_check_status_notification``, ``hostname_aop_custom_certificate_expiration_type``, ``http_alert_edge_error``, ``http_alert_origin_error``, ``image_notification``, ``image_resizing_notification``, ``incident_alert``, ``load_balancing_health_alert``, ``load_balancing_pool_enablement_alert``, ``logo_match_alert``, ``magic_tunnel_health_check_event``, ``maintenance_event_notification``, ``mtls_certificate_store_certificate_expiration_type``, ``pages_event_alert``, ``radar_notification``, ``real_origin_monitoring``, ``scriptmonitor_alert_new_code_change_detections``, ``scriptmonitor_alert_new_hosts``, ``scriptmonitor_alert_new_malicious_hosts``, ``scriptmonitor_alert_new_malicious_scripts``, ``scriptmonitor_alert_new_malicious_url``, ``scriptmonitor_alert_new_max_length_resource_url``, ``scriptmonitor_alert_new_resources``, ``secondary_dns_all_primaries_failing``, ``secondary_dns_primaries_failing``, ``secondary_dns_zone_successfully_updated``, ``secondary_dns_zone_validation_warning``, ``sentinel_alert``, ``stream_live_notifications``, ``traffic_anomalies_alert``, ``tunnel_health_event``, ``tunnel_update_event``, ``universal_ssl_event_type``, ``web_analytics_metrics_update``, ``weekly_account_overview``, ``workers_alert``, ``zone_aop_custom_certificate_expiration_type``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#alert_type NotificationPolicy#alert_type}
        '''
        result = self._values.get("alert_type")
        assert result is not None, "Required property 'alert_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''The status of the notification policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#enabled NotificationPolicy#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the notification policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#name NotificationPolicy#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the notification policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#description NotificationPolicy#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_integration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyEmailIntegration"]]]:
        '''email_integration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#email_integration NotificationPolicy#email_integration}
        '''
        result = self._values.get("email_integration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyEmailIntegration"]]], result)

    @builtins.property
    def filters(self) -> typing.Optional["NotificationPolicyFilters"]:
        '''filters block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#filters NotificationPolicy#filters}
        '''
        result = self._values.get("filters")
        return typing.cast(typing.Optional["NotificationPolicyFilters"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#id NotificationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pagerduty_integration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPagerdutyIntegration"]]]:
        '''pagerduty_integration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#pagerduty_integration NotificationPolicy#pagerduty_integration}
        '''
        result = self._values.get("pagerduty_integration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPagerdutyIntegration"]]], result)

    @builtins.property
    def webhooks_integration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyWebhooksIntegration"]]]:
        '''webhooks_integration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#webhooks_integration NotificationPolicy#webhooks_integration}
        '''
        result = self._values.get("webhooks_integration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyWebhooksIntegration"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyEmailIntegration",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class NotificationPolicyEmailIntegration:
    def __init__(
        self,
        *,
        id: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#name NotificationPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbd8bfa4ce5af6dd30a771ae2761e897ed7c1eda370c0bc7e944e0f6b390670b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#id NotificationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#name NotificationPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyEmailIntegration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NotificationPolicyEmailIntegrationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyEmailIntegrationList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__726916ea93533d47556c617d2a95159bbb338b8ece0f63d341ae3491e8aecc73)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NotificationPolicyEmailIntegrationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b84cf1853ce8fb1651091a60b9f6f597ca2eebaef5277861d62a43e3859f230)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NotificationPolicyEmailIntegrationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f71a49a0679a00f58d64945aa307b54d5d820cd89c99a8b1dd2ca3eef7822e7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ad15ec586fd42a696c881db8e9dc8e92bf26224406eeae4fc96190f42d49a8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d133a39151afe98acffa7635710f131fee5c7c0f99c9c21d75272daef31f3eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyEmailIntegration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyEmailIntegration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyEmailIntegration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e440d4191d07dc3c1fb064a04ba26bdd608eb0db24fb8cad690a7cc56d36d1fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class NotificationPolicyEmailIntegrationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyEmailIntegrationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83d43b2d3d2c25d3a68019ce625b62014280304ebaa31d44ff577c77b811a342)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d8f39d0e503d8cce663c5df63d9227224afebf58a9a778096186b9c7528d192)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0059b4eb4b5e9546efbb742a5d1cabce9e3ac458eff4d573e163e06cc00d752c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyEmailIntegration]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyEmailIntegration]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyEmailIntegration]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e57f38f3854a703d2d328b0afc90cdb90474ea9bcc5ba298c7fbba16a3eb1ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyFilters",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "affected_components": "affectedComponents",
        "airport_code": "airportCode",
        "alert_trigger_preferences": "alertTriggerPreferences",
        "enabled": "enabled",
        "environment": "environment",
        "event": "event",
        "event_source": "eventSource",
        "event_type": "eventType",
        "group_by": "groupBy",
        "health_check_id": "healthCheckId",
        "incident_impact": "incidentImpact",
        "input_id": "inputId",
        "limit": "limit",
        "megabits_per_second": "megabitsPerSecond",
        "new_health": "newHealth",
        "new_status": "newStatus",
        "packets_per_second": "packetsPerSecond",
        "pool_id": "poolId",
        "product": "product",
        "project_id": "projectId",
        "protocol": "protocol",
        "requests_per_second": "requestsPerSecond",
        "selectors": "selectors",
        "services": "services",
        "slo": "slo",
        "status": "status",
        "target_hostname": "targetHostname",
        "target_ip": "targetIp",
        "target_zone_name": "targetZoneName",
        "tunnel_id": "tunnelId",
        "tunnel_name": "tunnelName",
        "where": "where",
        "zones": "zones",
    },
)
class NotificationPolicyFilters:
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        affected_components: typing.Optional[typing.Sequence[builtins.str]] = None,
        airport_code: typing.Optional[typing.Sequence[builtins.str]] = None,
        alert_trigger_preferences: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Sequence[builtins.str]] = None,
        event: typing.Optional[typing.Sequence[builtins.str]] = None,
        event_source: typing.Optional[typing.Sequence[builtins.str]] = None,
        event_type: typing.Optional[typing.Sequence[builtins.str]] = None,
        group_by: typing.Optional[typing.Sequence[builtins.str]] = None,
        health_check_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        incident_impact: typing.Optional[typing.Sequence[builtins.str]] = None,
        input_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        limit: typing.Optional[typing.Sequence[builtins.str]] = None,
        megabits_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
        new_health: typing.Optional[typing.Sequence[builtins.str]] = None,
        new_status: typing.Optional[typing.Sequence[builtins.str]] = None,
        packets_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
        pool_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        product: typing.Optional[typing.Sequence[builtins.str]] = None,
        project_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        protocol: typing.Optional[typing.Sequence[builtins.str]] = None,
        requests_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
        selectors: typing.Optional[typing.Sequence[builtins.str]] = None,
        services: typing.Optional[typing.Sequence[builtins.str]] = None,
        slo: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_hostname: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_ip: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_zone_name: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel_id: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel_name: typing.Optional[typing.Sequence[builtins.str]] = None,
        where: typing.Optional[typing.Sequence[builtins.str]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param actions: Targeted actions for alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#actions NotificationPolicy#actions}
        :param affected_components: Affected components for alert. Available values: ``API``, ``API Shield``, ``Access``, ``Always Online``, ``Analytics``, ``Apps Marketplace``, ``Argo Smart Routing``, ``Audit Logs``, ``Authoritative DNS``, ``Billing``, ``Bot Management``, ``Bring Your Own IP (BYOIP)``, ``Browser Isolation``, ``CDN Cache Purge``, ``CDN/Cache``, ``Cache Reserve``, ``Challenge Platform``, ``Cloud Access Security Broker (CASB)``, ``Community Site``, ``D1``, ``DNS Root Servers``, ``DNS Updates``, ``Dashboard``, ``Data Loss Prevention (DLP)``, ``Developer's Site``, ``Digital Experience Monitoring (DEX)``, ``Distributed Web Gateway``, ``Durable Objects``, ``Email Routing``, ``Ethereum Gateway``, ``Firewall``, ``Gateway``, ``Geo-Key Manager``, ``Image Resizing``, ``Images``, ``Infrastructure``, ``Lists``, ``Load Balancing and Monitoring``, ``Logs``, ``Magic Firewall``, ``Magic Transit``, ``Magic WAN``, ``Magic WAN Connector``, ``Marketing Site``, ``Mirage``, ``Network``, ``Notifications``, ``Observatory``, ``Page Shield``, ``Pages``, ``R2``, ``Radar``, ``Randomness Beacon``, ``Recursive DNS``, ``Registrar``, ``Registration Data Access Protocol (RDAP)``, ``SSL Certificate Provisioning``, ``SSL for SaaS Provisioning``, ``Security Center``, ``Snippets``, ``Spectrum``, ``Speed Optimizations``, ``Stream``, ``Support Site``, ``Time Services``, ``Trace``, ``Tunnel``, ``Turnstile``, ``WARP``, ``Waiting Room``, ``Web Analytics``, ``Workers``, ``Workers KV``, ``Workers Preview``, ``Zaraz``, ``Zero Trust``, ``Zero Trust Dashboard``, ``Zone Versioning``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#affected_components NotificationPolicy#affected_components}
        :param airport_code: Filter on Points of Presence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#airport_code NotificationPolicy#airport_code}
        :param alert_trigger_preferences: Alert trigger preferences. Example: ``slo``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#alert_trigger_preferences NotificationPolicy#alert_trigger_preferences}
        :param enabled: State of the pool to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#enabled NotificationPolicy#enabled}
        :param environment: Environment of pages. Available values: ``ENVIRONMENT_PREVIEW``, ``ENVIRONMENT_PRODUCTION``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#environment NotificationPolicy#environment}
        :param event: Pages event to alert. Available values: ``EVENT_DEPLOYMENT_STARTED``, ``EVENT_DEPLOYMENT_FAILED``, ``EVENT_DEPLOYMENT_SUCCESS``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#event NotificationPolicy#event}
        :param event_source: Source configuration to alert on for pool or origin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#event_source NotificationPolicy#event_source}
        :param event_type: Stream event type to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#event_type NotificationPolicy#event_type}
        :param group_by: Alert grouping. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#group_by NotificationPolicy#group_by}
        :param health_check_id: Identifier health check. Required when using ``filters.0.status``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#health_check_id NotificationPolicy#health_check_id}
        :param incident_impact: The incident impact level that will trigger the dispatch of a notification. Available values: ``INCIDENT_IMPACT_NONE``, ``INCIDENT_IMPACT_MINOR``, ``INCIDENT_IMPACT_MAJOR``, ``INCIDENT_IMPACT_CRITICAL``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#incident_impact NotificationPolicy#incident_impact}
        :param input_id: Stream input id to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#input_id NotificationPolicy#input_id}
        :param limit: A numerical limit. Example: ``100``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#limit NotificationPolicy#limit}
        :param megabits_per_second: Megabits per second threshold for dos alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#megabits_per_second NotificationPolicy#megabits_per_second}
        :param new_health: Health status to alert on for pool or origin. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#new_health NotificationPolicy#new_health}
        :param new_status: Tunnel health status to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#new_status NotificationPolicy#new_status}
        :param packets_per_second: Packets per second threshold for dos alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#packets_per_second NotificationPolicy#packets_per_second}
        :param pool_id: Load balancer pool identifier. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#pool_id NotificationPolicy#pool_id}
        :param product: Product name. Available values: ``worker_requests``, ``worker_durable_objects_requests``, ``worker_durable_objects_duration``, ``worker_durable_objects_data_transfer``, ``worker_durable_objects_stored_data``, ``worker_durable_objects_storage_deletes``, ``worker_durable_objects_storage_writes``, ``worker_durable_objects_storage_reads``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#product NotificationPolicy#product}
        :param project_id: Identifier of pages project. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#project_id NotificationPolicy#project_id}
        :param protocol: Protocol to alert on for dos. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#protocol NotificationPolicy#protocol}
        :param requests_per_second: Requests per second threshold for dos alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#requests_per_second NotificationPolicy#requests_per_second}
        :param selectors: Selectors for alert. Valid options depend on the alert type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#selectors NotificationPolicy#selectors}
        :param services: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#services NotificationPolicy#services}.
        :param slo: A numerical limit. Example: ``99.9``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#slo NotificationPolicy#slo}
        :param status: Status to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#status NotificationPolicy#status}
        :param target_hostname: Target host to alert on for dos. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#target_hostname NotificationPolicy#target_hostname}
        :param target_ip: Target ip to alert on for dos in CIDR notation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#target_ip NotificationPolicy#target_ip}
        :param target_zone_name: Target domain to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#target_zone_name NotificationPolicy#target_zone_name}
        :param tunnel_id: Tunnel IDs to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#tunnel_id NotificationPolicy#tunnel_id}
        :param tunnel_name: Tunnel Names to alert on. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#tunnel_name NotificationPolicy#tunnel_name}
        :param where: Filter for alert. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#where NotificationPolicy#where}
        :param zones: A list of zone identifiers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#zones NotificationPolicy#zones}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5326ebf108453b36da8e814edd860719cbe2916d2193ee3d49f18c8694c6ff6)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument affected_components", value=affected_components, expected_type=type_hints["affected_components"])
            check_type(argname="argument airport_code", value=airport_code, expected_type=type_hints["airport_code"])
            check_type(argname="argument alert_trigger_preferences", value=alert_trigger_preferences, expected_type=type_hints["alert_trigger_preferences"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument event_source", value=event_source, expected_type=type_hints["event_source"])
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument group_by", value=group_by, expected_type=type_hints["group_by"])
            check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
            check_type(argname="argument incident_impact", value=incident_impact, expected_type=type_hints["incident_impact"])
            check_type(argname="argument input_id", value=input_id, expected_type=type_hints["input_id"])
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
            check_type(argname="argument megabits_per_second", value=megabits_per_second, expected_type=type_hints["megabits_per_second"])
            check_type(argname="argument new_health", value=new_health, expected_type=type_hints["new_health"])
            check_type(argname="argument new_status", value=new_status, expected_type=type_hints["new_status"])
            check_type(argname="argument packets_per_second", value=packets_per_second, expected_type=type_hints["packets_per_second"])
            check_type(argname="argument pool_id", value=pool_id, expected_type=type_hints["pool_id"])
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument requests_per_second", value=requests_per_second, expected_type=type_hints["requests_per_second"])
            check_type(argname="argument selectors", value=selectors, expected_type=type_hints["selectors"])
            check_type(argname="argument services", value=services, expected_type=type_hints["services"])
            check_type(argname="argument slo", value=slo, expected_type=type_hints["slo"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument target_hostname", value=target_hostname, expected_type=type_hints["target_hostname"])
            check_type(argname="argument target_ip", value=target_ip, expected_type=type_hints["target_ip"])
            check_type(argname="argument target_zone_name", value=target_zone_name, expected_type=type_hints["target_zone_name"])
            check_type(argname="argument tunnel_id", value=tunnel_id, expected_type=type_hints["tunnel_id"])
            check_type(argname="argument tunnel_name", value=tunnel_name, expected_type=type_hints["tunnel_name"])
            check_type(argname="argument where", value=where, expected_type=type_hints["where"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if actions is not None:
            self._values["actions"] = actions
        if affected_components is not None:
            self._values["affected_components"] = affected_components
        if airport_code is not None:
            self._values["airport_code"] = airport_code
        if alert_trigger_preferences is not None:
            self._values["alert_trigger_preferences"] = alert_trigger_preferences
        if enabled is not None:
            self._values["enabled"] = enabled
        if environment is not None:
            self._values["environment"] = environment
        if event is not None:
            self._values["event"] = event
        if event_source is not None:
            self._values["event_source"] = event_source
        if event_type is not None:
            self._values["event_type"] = event_type
        if group_by is not None:
            self._values["group_by"] = group_by
        if health_check_id is not None:
            self._values["health_check_id"] = health_check_id
        if incident_impact is not None:
            self._values["incident_impact"] = incident_impact
        if input_id is not None:
            self._values["input_id"] = input_id
        if limit is not None:
            self._values["limit"] = limit
        if megabits_per_second is not None:
            self._values["megabits_per_second"] = megabits_per_second
        if new_health is not None:
            self._values["new_health"] = new_health
        if new_status is not None:
            self._values["new_status"] = new_status
        if packets_per_second is not None:
            self._values["packets_per_second"] = packets_per_second
        if pool_id is not None:
            self._values["pool_id"] = pool_id
        if product is not None:
            self._values["product"] = product
        if project_id is not None:
            self._values["project_id"] = project_id
        if protocol is not None:
            self._values["protocol"] = protocol
        if requests_per_second is not None:
            self._values["requests_per_second"] = requests_per_second
        if selectors is not None:
            self._values["selectors"] = selectors
        if services is not None:
            self._values["services"] = services
        if slo is not None:
            self._values["slo"] = slo
        if status is not None:
            self._values["status"] = status
        if target_hostname is not None:
            self._values["target_hostname"] = target_hostname
        if target_ip is not None:
            self._values["target_ip"] = target_ip
        if target_zone_name is not None:
            self._values["target_zone_name"] = target_zone_name
        if tunnel_id is not None:
            self._values["tunnel_id"] = tunnel_id
        if tunnel_name is not None:
            self._values["tunnel_name"] = tunnel_name
        if where is not None:
            self._values["where"] = where
        if zones is not None:
            self._values["zones"] = zones

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Targeted actions for alert.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#actions NotificationPolicy#actions}
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def affected_components(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Affected components for alert.

        Available values: ``API``, ``API Shield``, ``Access``, ``Always Online``, ``Analytics``, ``Apps Marketplace``, ``Argo Smart Routing``, ``Audit Logs``, ``Authoritative DNS``, ``Billing``, ``Bot Management``, ``Bring Your Own IP (BYOIP)``, ``Browser Isolation``, ``CDN Cache Purge``, ``CDN/Cache``, ``Cache Reserve``, ``Challenge Platform``, ``Cloud Access Security Broker (CASB)``, ``Community Site``, ``D1``, ``DNS Root Servers``, ``DNS Updates``, ``Dashboard``, ``Data Loss Prevention (DLP)``, ``Developer's Site``, ``Digital Experience Monitoring (DEX)``, ``Distributed Web Gateway``, ``Durable Objects``, ``Email Routing``, ``Ethereum Gateway``, ``Firewall``, ``Gateway``, ``Geo-Key Manager``, ``Image Resizing``, ``Images``, ``Infrastructure``, ``Lists``, ``Load Balancing and Monitoring``, ``Logs``, ``Magic Firewall``, ``Magic Transit``, ``Magic WAN``, ``Magic WAN Connector``, ``Marketing Site``, ``Mirage``, ``Network``, ``Notifications``, ``Observatory``, ``Page Shield``, ``Pages``, ``R2``, ``Radar``, ``Randomness Beacon``, ``Recursive DNS``, ``Registrar``, ``Registration Data Access Protocol (RDAP)``, ``SSL Certificate Provisioning``, ``SSL for SaaS Provisioning``, ``Security Center``, ``Snippets``, ``Spectrum``, ``Speed Optimizations``, ``Stream``, ``Support Site``, ``Time Services``, ``Trace``, ``Tunnel``, ``Turnstile``, ``WARP``, ``Waiting Room``, ``Web Analytics``, ``Workers``, ``Workers KV``, ``Workers Preview``, ``Zaraz``, ``Zero Trust``, ``Zero Trust Dashboard``, ``Zone Versioning``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#affected_components NotificationPolicy#affected_components}
        '''
        result = self._values.get("affected_components")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def airport_code(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Filter on Points of Presence.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#airport_code NotificationPolicy#airport_code}
        '''
        result = self._values.get("airport_code")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def alert_trigger_preferences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alert trigger preferences. Example: ``slo``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#alert_trigger_preferences NotificationPolicy#alert_trigger_preferences}
        '''
        result = self._values.get("alert_trigger_preferences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[typing.List[builtins.str]]:
        '''State of the pool to alert on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#enabled NotificationPolicy#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def environment(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Environment of pages. Available values: ``ENVIRONMENT_PREVIEW``, ``ENVIRONMENT_PRODUCTION``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#environment NotificationPolicy#environment}
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def event(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Pages event to alert. Available values: ``EVENT_DEPLOYMENT_STARTED``, ``EVENT_DEPLOYMENT_FAILED``, ``EVENT_DEPLOYMENT_SUCCESS``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#event NotificationPolicy#event}
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def event_source(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Source configuration to alert on for pool or origin.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#event_source NotificationPolicy#event_source}
        '''
        result = self._values.get("event_source")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def event_type(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Stream event type to alert on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#event_type NotificationPolicy#event_type}
        '''
        result = self._values.get("event_type")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def group_by(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alert grouping.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#group_by NotificationPolicy#group_by}
        '''
        result = self._values.get("group_by")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def health_check_id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Identifier health check. Required when using ``filters.0.status``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#health_check_id NotificationPolicy#health_check_id}
        '''
        result = self._values.get("health_check_id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def incident_impact(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The incident impact level that will trigger the dispatch of a notification. Available values: ``INCIDENT_IMPACT_NONE``, ``INCIDENT_IMPACT_MINOR``, ``INCIDENT_IMPACT_MAJOR``, ``INCIDENT_IMPACT_CRITICAL``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#incident_impact NotificationPolicy#incident_impact}
        '''
        result = self._values.get("incident_impact")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def input_id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Stream input id to alert on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#input_id NotificationPolicy#input_id}
        '''
        result = self._values.get("input_id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def limit(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A numerical limit. Example: ``100``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#limit NotificationPolicy#limit}
        '''
        result = self._values.get("limit")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def megabits_per_second(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Megabits per second threshold for dos alert.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#megabits_per_second NotificationPolicy#megabits_per_second}
        '''
        result = self._values.get("megabits_per_second")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def new_health(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Health status to alert on for pool or origin.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#new_health NotificationPolicy#new_health}
        '''
        result = self._values.get("new_health")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def new_status(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tunnel health status to alert on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#new_status NotificationPolicy#new_status}
        '''
        result = self._values.get("new_status")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def packets_per_second(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Packets per second threshold for dos alert.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#packets_per_second NotificationPolicy#packets_per_second}
        '''
        result = self._values.get("packets_per_second")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def pool_id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Load balancer pool identifier.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#pool_id NotificationPolicy#pool_id}
        '''
        result = self._values.get("pool_id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def product(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Product name. Available values: ``worker_requests``, ``worker_durable_objects_requests``, ``worker_durable_objects_duration``, ``worker_durable_objects_data_transfer``, ``worker_durable_objects_stored_data``, ``worker_durable_objects_storage_deletes``, ``worker_durable_objects_storage_writes``, ``worker_durable_objects_storage_reads``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#product NotificationPolicy#product}
        '''
        result = self._values.get("product")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def project_id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Identifier of pages project.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#project_id NotificationPolicy#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def protocol(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Protocol to alert on for dos.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#protocol NotificationPolicy#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def requests_per_second(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Requests per second threshold for dos alert.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#requests_per_second NotificationPolicy#requests_per_second}
        '''
        result = self._values.get("requests_per_second")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def selectors(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Selectors for alert. Valid options depend on the alert type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#selectors NotificationPolicy#selectors}
        '''
        result = self._values.get("selectors")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#services NotificationPolicy#services}.'''
        result = self._values.get("services")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slo(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A numerical limit. Example: ``99.9``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#slo NotificationPolicy#slo}
        '''
        result = self._values.get("slo")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Status to alert on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#status NotificationPolicy#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_hostname(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Target host to alert on for dos.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#target_hostname NotificationPolicy#target_hostname}
        '''
        result = self._values.get("target_hostname")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_ip(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Target ip to alert on for dos in CIDR notation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#target_ip NotificationPolicy#target_ip}
        '''
        result = self._values.get("target_ip")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_zone_name(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Target domain to alert on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#target_zone_name NotificationPolicy#target_zone_name}
        '''
        result = self._values.get("target_zone_name")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel_id(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tunnel IDs to alert on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#tunnel_id NotificationPolicy#tunnel_id}
        '''
        result = self._values.get("tunnel_id")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel_name(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tunnel Names to alert on.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#tunnel_name NotificationPolicy#tunnel_name}
        '''
        result = self._values.get("tunnel_name")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def where(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Filter for alert.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#where NotificationPolicy#where}
        '''
        result = self._values.get("where")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of zone identifiers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#zones NotificationPolicy#zones}
        '''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyFilters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NotificationPolicyFiltersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyFiltersOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8f31f649dafa1c3b6903338e913d967b05f75e2592e91fc18bbbf5a9a72cbcb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetActions")
    def reset_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActions", []))

    @jsii.member(jsii_name="resetAffectedComponents")
    def reset_affected_components(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAffectedComponents", []))

    @jsii.member(jsii_name="resetAirportCode")
    def reset_airport_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAirportCode", []))

    @jsii.member(jsii_name="resetAlertTriggerPreferences")
    def reset_alert_trigger_preferences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertTriggerPreferences", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @jsii.member(jsii_name="resetEvent")
    def reset_event(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvent", []))

    @jsii.member(jsii_name="resetEventSource")
    def reset_event_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventSource", []))

    @jsii.member(jsii_name="resetEventType")
    def reset_event_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventType", []))

    @jsii.member(jsii_name="resetGroupBy")
    def reset_group_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupBy", []))

    @jsii.member(jsii_name="resetHealthCheckId")
    def reset_health_check_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckId", []))

    @jsii.member(jsii_name="resetIncidentImpact")
    def reset_incident_impact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncidentImpact", []))

    @jsii.member(jsii_name="resetInputId")
    def reset_input_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputId", []))

    @jsii.member(jsii_name="resetLimit")
    def reset_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLimit", []))

    @jsii.member(jsii_name="resetMegabitsPerSecond")
    def reset_megabits_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMegabitsPerSecond", []))

    @jsii.member(jsii_name="resetNewHealth")
    def reset_new_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewHealth", []))

    @jsii.member(jsii_name="resetNewStatus")
    def reset_new_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewStatus", []))

    @jsii.member(jsii_name="resetPacketsPerSecond")
    def reset_packets_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPacketsPerSecond", []))

    @jsii.member(jsii_name="resetPoolId")
    def reset_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPoolId", []))

    @jsii.member(jsii_name="resetProduct")
    def reset_product(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProduct", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetRequestsPerSecond")
    def reset_requests_per_second(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestsPerSecond", []))

    @jsii.member(jsii_name="resetSelectors")
    def reset_selectors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectors", []))

    @jsii.member(jsii_name="resetServices")
    def reset_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServices", []))

    @jsii.member(jsii_name="resetSlo")
    def reset_slo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlo", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetTargetHostname")
    def reset_target_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetHostname", []))

    @jsii.member(jsii_name="resetTargetIp")
    def reset_target_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetIp", []))

    @jsii.member(jsii_name="resetTargetZoneName")
    def reset_target_zone_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetZoneName", []))

    @jsii.member(jsii_name="resetTunnelId")
    def reset_tunnel_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnelId", []))

    @jsii.member(jsii_name="resetTunnelName")
    def reset_tunnel_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnelName", []))

    @jsii.member(jsii_name="resetWhere")
    def reset_where(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhere", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="affectedComponentsInput")
    def affected_components_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "affectedComponentsInput"))

    @builtins.property
    @jsii.member(jsii_name="airportCodeInput")
    def airport_code_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "airportCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="alertTriggerPreferencesInput")
    def alert_trigger_preferences_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alertTriggerPreferencesInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="eventInput")
    def event_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventInput"))

    @builtins.property
    @jsii.member(jsii_name="eventSourceInput")
    def event_source_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="eventTypeInput")
    def event_type_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByInput")
    def group_by_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckIdInput")
    def health_check_id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "healthCheckIdInput"))

    @builtins.property
    @jsii.member(jsii_name="incidentImpactInput")
    def incident_impact_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "incidentImpactInput"))

    @builtins.property
    @jsii.member(jsii_name="inputIdInput")
    def input_id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "inputIdInput"))

    @builtins.property
    @jsii.member(jsii_name="limitInput")
    def limit_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "limitInput"))

    @builtins.property
    @jsii.member(jsii_name="megabitsPerSecondInput")
    def megabits_per_second_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "megabitsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="newHealthInput")
    def new_health_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "newHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="newStatusInput")
    def new_status_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "newStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="packetsPerSecondInput")
    def packets_per_second_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "packetsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="poolIdInput")
    def pool_id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "poolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="productInput")
    def product_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "productInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="requestsPerSecondInput")
    def requests_per_second_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requestsPerSecondInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorsInput")
    def selectors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "selectorsInput"))

    @builtins.property
    @jsii.member(jsii_name="servicesInput")
    def services_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "servicesInput"))

    @builtins.property
    @jsii.member(jsii_name="sloInput")
    def slo_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sloInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="targetHostnameInput")
    def target_hostname_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetIpInput")
    def target_ip_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetIpInput"))

    @builtins.property
    @jsii.member(jsii_name="targetZoneNameInput")
    def target_zone_name_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetZoneNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnelIdInput")
    def tunnel_id_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnelIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnelNameInput")
    def tunnel_name_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="whereInput")
    def where_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "whereInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actions"))

    @actions.setter
    def actions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cbd740b090d5dcb3f98c1a4b6ff1a0651678c49b1243b284e7acc76e721589c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="affectedComponents")
    def affected_components(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "affectedComponents"))

    @affected_components.setter
    def affected_components(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__115da5f87a19dafbf96877c6df454a434fa82dee931e598988a1c5ff0eca9fa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "affectedComponents", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="airportCode")
    def airport_code(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "airportCode"))

    @airport_code.setter
    def airport_code(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d941b7b7c50ceac8552ec74cb449a272d2e6a82dbca9e8d05722e7093b8aa012)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "airportCode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="alertTriggerPreferences")
    def alert_trigger_preferences(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "alertTriggerPreferences"))

    @alert_trigger_preferences.setter
    def alert_trigger_preferences(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a8320bc1ab0055c005acf8e4d040f5ec3002105ebf206ab47f5525b66cdf017)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertTriggerPreferences", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b6ee8a77ab98e8abcf11477f1b4e4218a4a26478a7b259ee789af85016e8618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb0a14683d0f88547af387c7869591ec8197b90a02b0892486f5d8c23ef17565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="event")
    def event(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "event"))

    @event.setter
    def event(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a4a91dd52f49b0fec512d8e17d8b8240f99bc3f39fa0ee67625df8dace723e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "event", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventSource")
    def event_source(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eventSource"))

    @event_source.setter
    def event_source(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3df89f3b37f251c30996df91f244b0e38e4c03fd32e227ef4866d53db10c4f71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventSource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86846fba85173ea61eaef275166914e708d9a78cc98774322e89a5507120a689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="groupBy")
    def group_by(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupBy"))

    @group_by.setter
    def group_by(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e978f4cf3db6c6b55f6b53bb973d85fa4170a68f295507309a67a4f395b50c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupBy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="healthCheckId")
    def health_check_id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "healthCheckId"))

    @health_check_id.setter
    def health_check_id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c36e1d871dafdc1ec7b5ca7ef3c1e55d5e3fffff205f8f6e393e16559a71d94a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="incidentImpact")
    def incident_impact(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "incidentImpact"))

    @incident_impact.setter
    def incident_impact(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13313e393833d80e078d2cd462aff18800b7798f22b77741274bf92e597618cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "incidentImpact", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="inputId")
    def input_id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "inputId"))

    @input_id.setter
    def input_id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13749ce4d14ee4d47ca2b743593e0ea6f8c5d1e90db0b4187cef46c6281fc868)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="limit")
    def limit(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "limit"))

    @limit.setter
    def limit(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c7cb06df8ae94848c7d39371bb6bd7cafdd6893fc1fa40c3e9a95e769691bbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "limit", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="megabitsPerSecond")
    def megabits_per_second(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "megabitsPerSecond"))

    @megabits_per_second.setter
    def megabits_per_second(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2e46433a07b7996ca9c557720a807d2654d178508bcf210b8a79c277a55678d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "megabitsPerSecond", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="newHealth")
    def new_health(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "newHealth"))

    @new_health.setter
    def new_health(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__966097109aab71dd336a62096323ee6c5a20d6f9e5eb6ad3da692d10466d7f30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newHealth", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="newStatus")
    def new_status(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "newStatus"))

    @new_status.setter
    def new_status(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9d1aedf12f36c5e87a2c7c4dd88494cd6c4ed2ef80edab2f726408ac75ffa3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newStatus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="packetsPerSecond")
    def packets_per_second(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "packetsPerSecond"))

    @packets_per_second.setter
    def packets_per_second(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5426e77e9e8c318d485d667eeae7786bf21d76bb73e66167a78b6e56bd60a267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packetsPerSecond", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="poolId")
    def pool_id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "poolId"))

    @pool_id.setter
    def pool_id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc505ad097f5dfa3183501da19ee617059ab758a68300726c93efd8db22c9581)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "product"))

    @product.setter
    def product(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2734761a5311a1478499b1a47a670c6c381a85a844cad3ede6ff97dd200176c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00c01b98586d5f97b73f117d41a62c0b7ee62fdc73706705cda00665cc6fe996)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb8231efaeb8ff5412b70a100e1e1e8fe333cd173c99bba7c99c2add01119d6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="requestsPerSecond")
    def requests_per_second(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requestsPerSecond"))

    @requests_per_second.setter
    def requests_per_second(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0210adff9def3da2b344737aced573e739cc90b4b559ab475c8dcf6ad23fcce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestsPerSecond", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="selectors")
    def selectors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "selectors"))

    @selectors.setter
    def selectors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc62169f354fdaea6f58699f464b357e6594dfba5c9b5213d1e9c8e6e093a980)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectors", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="services")
    def services(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "services"))

    @services.setter
    def services(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38946182c0876ef8edde111dcf158bdfa520e63003a1842b6d12b654e0811177)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "services", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="slo")
    def slo(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "slo"))

    @slo.setter
    def slo(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddac2950663962abc49fa4b4a3de241a9dc8347bc8504783957b28abed41bc26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slo", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc5e44de392b4c9224fa1e9e69a47d71fe69a9b09a5f72294f83d7b44ae057e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetHostname")
    def target_hostname(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetHostname"))

    @target_hostname.setter
    def target_hostname(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ee145ec9ca264bfd11e1e013c478b3e6a8c893d6acce284138697a69c109afa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetHostname", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetIp")
    def target_ip(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetIp"))

    @target_ip.setter
    def target_ip(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1efa3e3d8317d012dba9b2b9a4f09b288d162b18f556ccb80f040e7519ec04db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetIp", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetZoneName")
    def target_zone_name(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetZoneName"))

    @target_zone_name.setter
    def target_zone_name(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__929a1c9b8b107397727ee7bcaa081ba130753718ffe3fd830d9854fd007b171a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetZoneName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tunnelId")
    def tunnel_id(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnelId"))

    @tunnel_id.setter
    def tunnel_id(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ea02582293c26043e9546d2e9124ee900459a5719e024032bfee8893a039071)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnelId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tunnelName")
    def tunnel_name(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnelName"))

    @tunnel_name.setter
    def tunnel_name(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eea45a5a7c3cd29b86a701dfbac6025ea8efa606b3016108959b7a5718f5c16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnelName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="where")
    def where(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "where"))

    @where.setter
    def where(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0125865a7a67cb69fbb62c26e94245929beab4f8931d71649d8fb0abd7233f9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "where", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fb662b6bb44dcbe00b0cb7d46a78ad122a89d20f0f4ef981e54665d2a423f6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NotificationPolicyFilters]:
        return typing.cast(typing.Optional[NotificationPolicyFilters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NotificationPolicyFilters]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90a7709fbc2441ad30314af92ed6b3df73d6f83c4a876a9bfa7366752bf3ab12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyPagerdutyIntegration",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class NotificationPolicyPagerdutyIntegration:
    def __init__(
        self,
        *,
        id: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#name NotificationPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__098b053c39139932375fb51ba3cb8f60a3e8634fd2c96773e5e351c0d361bead)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#id NotificationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#name NotificationPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyPagerdutyIntegration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NotificationPolicyPagerdutyIntegrationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyPagerdutyIntegrationList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf0b60c060e36df5dd453365e10042319495f55c567c4e814e3fe020a3761d30)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NotificationPolicyPagerdutyIntegrationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__332446f9a9350e54e7d531ee6b65c98b142dffda6a76876fe79750190d446efd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NotificationPolicyPagerdutyIntegrationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08f16e05df473d1bd80981ba7110c8005d1e63989e04a9c3078ee23e685d7645)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34cdd22d91ccca9f1f5465ab66a89245f87b998fa65e4f9bea766049162dcf50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19e37aa777d8b7de8d088c5d967b48ff6199d8e68fa58c7b569962279ce920c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPagerdutyIntegration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPagerdutyIntegration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPagerdutyIntegration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2172f96f29888f02c6f289836c5f6de01a904cc1f60925aa790d1cdfd6e568d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class NotificationPolicyPagerdutyIntegrationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyPagerdutyIntegrationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62646b2686cb0cee153a5821ba8e0df5b17e208f27f57a52031ffb88e1ec21ad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d872ca6f7e72efc4eaf291aa085ceac5730bf943fb8cc9be06a4efcdb9a1bc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14209f5c16a0d4af6b24b0bbc00efa979f1910bf5872c943c589a181ab183176)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyPagerdutyIntegration]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyPagerdutyIntegration]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyPagerdutyIntegration]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee550419c38f6e7eac8ff45bd56e15957d328f3dc2e366610b2c830d127c512e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyWebhooksIntegration",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class NotificationPolicyWebhooksIntegration:
    def __init__(
        self,
        *,
        id: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#name NotificationPolicy#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__258d023569651f49c9a0ef8754f2acc85563df208a3d211afd6fd16f8cf1d233)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#id NotificationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/cloudflare/cloudflare/4.52.0/docs/resources/notification_policy#name NotificationPolicy#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyWebhooksIntegration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NotificationPolicyWebhooksIntegrationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyWebhooksIntegrationList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81b0a7c90f1ac8e2dca016ed7b1ff17bae37497d43e9ec3f1d837701295a78e9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NotificationPolicyWebhooksIntegrationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40304512fb180704391335d0cd3945d708438ded21ea118e9c8d7e94fc5c252e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NotificationPolicyWebhooksIntegrationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b97787639adff1d793085035bab6454cec45db5d77e23bf26e1540c195039db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90c8e49b57d54d73e8b992c50a3455fd55dc0ecb23cdf1fd52dccda6b80b5162)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7f2d279ae511c82a13f8d8576726900198da9d47e5fc84e86089c6038191319)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyWebhooksIntegration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyWebhooksIntegration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyWebhooksIntegration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00fe6bdd8f487c8357ece56ba834b085434cb1ac17d30d641ebf2de7aba4dc34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class NotificationPolicyWebhooksIntegrationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.notificationPolicy.NotificationPolicyWebhooksIntegrationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09570917e5937ea65e4c6e340e86776ea1f0acfdf7a62c3c2a9c8fc712c9fdc2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3024ecaf47fad063f4cca152ae32ea9e27c96dbd4455ba841f9fdae858639da8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8812fd2040bd87724281811ebced61ba00e5a73bed5cae5c1db3a2a4e1859ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyWebhooksIntegration]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyWebhooksIntegration]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyWebhooksIntegration]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b025e6c9620e926c1b00efb1c1b86166c7e242632537a4552f32266f831ff76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "NotificationPolicy",
    "NotificationPolicyConfig",
    "NotificationPolicyEmailIntegration",
    "NotificationPolicyEmailIntegrationList",
    "NotificationPolicyEmailIntegrationOutputReference",
    "NotificationPolicyFilters",
    "NotificationPolicyFiltersOutputReference",
    "NotificationPolicyPagerdutyIntegration",
    "NotificationPolicyPagerdutyIntegrationList",
    "NotificationPolicyPagerdutyIntegrationOutputReference",
    "NotificationPolicyWebhooksIntegration",
    "NotificationPolicyWebhooksIntegrationList",
    "NotificationPolicyWebhooksIntegrationOutputReference",
]

publication.publish()

def _typecheckingstub__d26986a49b23bd0b8c252e62235f69de0aed407a858eb18dec93b2afb89ac0f4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    account_id: builtins.str,
    alert_type: builtins.str,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    email_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyEmailIntegration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    filters: typing.Optional[typing.Union[NotificationPolicyFilters, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    pagerduty_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPagerdutyIntegration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    webhooks_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyWebhooksIntegration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__125b1431b5b31917f637f01b7497a9caaaa8b98ffa586ee484008a61b146f960(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2609648347639c71060c162127a890fa79f5aa754008f528fe5bd16e169c51c2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyEmailIntegration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e6d605bc183299465ed36999e058ed339c1c1d9d4260aabb5d8121c2decd657(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPagerdutyIntegration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcdb11383bda2c3b10780c02c32f0e2dfdfb687da0c11a00120f0b6ad6661f78(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyWebhooksIntegration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d61495632773ce0d55188dd5c264531790da548ad26191efd65e253d9ad7eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c59bc8c4d370898c433afe11d54353dbb01e0117c5e68b0ebcca68e7bcdf69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df1ca562165db15d390fd123cc403797076f4dd2d4772623a50ab8a708b70143(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b59f2fa90359289bd4f53cbe0d77c9cf06b5a6eee45e84f5d1ad1ad9d7481c80(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46a33d76b4aab3bd5c657ec06950c493c424c61455616973e446696aa8e28398(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c32685b847789725af6a3b296bc5149261a762977bb9e1060f4aedc88b42c842(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bfdad0ea3b671f6ddd7c3f93399e6b1e1dbbec330f6748078f80895b3d1a900(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    account_id: builtins.str,
    alert_type: builtins.str,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    email_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyEmailIntegration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    filters: typing.Optional[typing.Union[NotificationPolicyFilters, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    pagerduty_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPagerdutyIntegration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    webhooks_integration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyWebhooksIntegration, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbd8bfa4ce5af6dd30a771ae2761e897ed7c1eda370c0bc7e944e0f6b390670b(
    *,
    id: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__726916ea93533d47556c617d2a95159bbb338b8ece0f63d341ae3491e8aecc73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b84cf1853ce8fb1651091a60b9f6f597ca2eebaef5277861d62a43e3859f230(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f71a49a0679a00f58d64945aa307b54d5d820cd89c99a8b1dd2ca3eef7822e7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ad15ec586fd42a696c881db8e9dc8e92bf26224406eeae4fc96190f42d49a8e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d133a39151afe98acffa7635710f131fee5c7c0f99c9c21d75272daef31f3eb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e440d4191d07dc3c1fb064a04ba26bdd608eb0db24fb8cad690a7cc56d36d1fb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyEmailIntegration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83d43b2d3d2c25d3a68019ce625b62014280304ebaa31d44ff577c77b811a342(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d8f39d0e503d8cce663c5df63d9227224afebf58a9a778096186b9c7528d192(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0059b4eb4b5e9546efbb742a5d1cabce9e3ac458eff4d573e163e06cc00d752c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e57f38f3854a703d2d328b0afc90cdb90474ea9bcc5ba298c7fbba16a3eb1ac(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyEmailIntegration]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5326ebf108453b36da8e814edd860719cbe2916d2193ee3d49f18c8694c6ff6(
    *,
    actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    affected_components: typing.Optional[typing.Sequence[builtins.str]] = None,
    airport_code: typing.Optional[typing.Sequence[builtins.str]] = None,
    alert_trigger_preferences: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[typing.Sequence[builtins.str]] = None,
    environment: typing.Optional[typing.Sequence[builtins.str]] = None,
    event: typing.Optional[typing.Sequence[builtins.str]] = None,
    event_source: typing.Optional[typing.Sequence[builtins.str]] = None,
    event_type: typing.Optional[typing.Sequence[builtins.str]] = None,
    group_by: typing.Optional[typing.Sequence[builtins.str]] = None,
    health_check_id: typing.Optional[typing.Sequence[builtins.str]] = None,
    incident_impact: typing.Optional[typing.Sequence[builtins.str]] = None,
    input_id: typing.Optional[typing.Sequence[builtins.str]] = None,
    limit: typing.Optional[typing.Sequence[builtins.str]] = None,
    megabits_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
    new_health: typing.Optional[typing.Sequence[builtins.str]] = None,
    new_status: typing.Optional[typing.Sequence[builtins.str]] = None,
    packets_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
    pool_id: typing.Optional[typing.Sequence[builtins.str]] = None,
    product: typing.Optional[typing.Sequence[builtins.str]] = None,
    project_id: typing.Optional[typing.Sequence[builtins.str]] = None,
    protocol: typing.Optional[typing.Sequence[builtins.str]] = None,
    requests_per_second: typing.Optional[typing.Sequence[builtins.str]] = None,
    selectors: typing.Optional[typing.Sequence[builtins.str]] = None,
    services: typing.Optional[typing.Sequence[builtins.str]] = None,
    slo: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[typing.Sequence[builtins.str]] = None,
    target_hostname: typing.Optional[typing.Sequence[builtins.str]] = None,
    target_ip: typing.Optional[typing.Sequence[builtins.str]] = None,
    target_zone_name: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel_id: typing.Optional[typing.Sequence[builtins.str]] = None,
    tunnel_name: typing.Optional[typing.Sequence[builtins.str]] = None,
    where: typing.Optional[typing.Sequence[builtins.str]] = None,
    zones: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f31f649dafa1c3b6903338e913d967b05f75e2592e91fc18bbbf5a9a72cbcb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cbd740b090d5dcb3f98c1a4b6ff1a0651678c49b1243b284e7acc76e721589c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115da5f87a19dafbf96877c6df454a434fa82dee931e598988a1c5ff0eca9fa9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d941b7b7c50ceac8552ec74cb449a272d2e6a82dbca9e8d05722e7093b8aa012(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a8320bc1ab0055c005acf8e4d040f5ec3002105ebf206ab47f5525b66cdf017(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b6ee8a77ab98e8abcf11477f1b4e4218a4a26478a7b259ee789af85016e8618(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb0a14683d0f88547af387c7869591ec8197b90a02b0892486f5d8c23ef17565(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4a91dd52f49b0fec512d8e17d8b8240f99bc3f39fa0ee67625df8dace723e4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3df89f3b37f251c30996df91f244b0e38e4c03fd32e227ef4866d53db10c4f71(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86846fba85173ea61eaef275166914e708d9a78cc98774322e89a5507120a689(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e978f4cf3db6c6b55f6b53bb973d85fa4170a68f295507309a67a4f395b50c7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c36e1d871dafdc1ec7b5ca7ef3c1e55d5e3fffff205f8f6e393e16559a71d94a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13313e393833d80e078d2cd462aff18800b7798f22b77741274bf92e597618cb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13749ce4d14ee4d47ca2b743593e0ea6f8c5d1e90db0b4187cef46c6281fc868(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c7cb06df8ae94848c7d39371bb6bd7cafdd6893fc1fa40c3e9a95e769691bbb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2e46433a07b7996ca9c557720a807d2654d178508bcf210b8a79c277a55678d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__966097109aab71dd336a62096323ee6c5a20d6f9e5eb6ad3da692d10466d7f30(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d1aedf12f36c5e87a2c7c4dd88494cd6c4ed2ef80edab2f726408ac75ffa3c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5426e77e9e8c318d485d667eeae7786bf21d76bb73e66167a78b6e56bd60a267(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc505ad097f5dfa3183501da19ee617059ab758a68300726c93efd8db22c9581(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2734761a5311a1478499b1a47a670c6c381a85a844cad3ede6ff97dd200176c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00c01b98586d5f97b73f117d41a62c0b7ee62fdc73706705cda00665cc6fe996(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb8231efaeb8ff5412b70a100e1e1e8fe333cd173c99bba7c99c2add01119d6e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0210adff9def3da2b344737aced573e739cc90b4b559ab475c8dcf6ad23fcce2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc62169f354fdaea6f58699f464b357e6594dfba5c9b5213d1e9c8e6e093a980(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38946182c0876ef8edde111dcf158bdfa520e63003a1842b6d12b654e0811177(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddac2950663962abc49fa4b4a3de241a9dc8347bc8504783957b28abed41bc26(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc5e44de392b4c9224fa1e9e69a47d71fe69a9b09a5f72294f83d7b44ae057e7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee145ec9ca264bfd11e1e013c478b3e6a8c893d6acce284138697a69c109afa(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1efa3e3d8317d012dba9b2b9a4f09b288d162b18f556ccb80f040e7519ec04db(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__929a1c9b8b107397727ee7bcaa081ba130753718ffe3fd830d9854fd007b171a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea02582293c26043e9546d2e9124ee900459a5719e024032bfee8893a039071(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eea45a5a7c3cd29b86a701dfbac6025ea8efa606b3016108959b7a5718f5c16(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0125865a7a67cb69fbb62c26e94245929beab4f8931d71649d8fb0abd7233f9f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fb662b6bb44dcbe00b0cb7d46a78ad122a89d20f0f4ef981e54665d2a423f6e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a7709fbc2441ad30314af92ed6b3df73d6f83c4a876a9bfa7366752bf3ab12(
    value: typing.Optional[NotificationPolicyFilters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__098b053c39139932375fb51ba3cb8f60a3e8634fd2c96773e5e351c0d361bead(
    *,
    id: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf0b60c060e36df5dd453365e10042319495f55c567c4e814e3fe020a3761d30(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332446f9a9350e54e7d531ee6b65c98b142dffda6a76876fe79750190d446efd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08f16e05df473d1bd80981ba7110c8005d1e63989e04a9c3078ee23e685d7645(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34cdd22d91ccca9f1f5465ab66a89245f87b998fa65e4f9bea766049162dcf50(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19e37aa777d8b7de8d088c5d967b48ff6199d8e68fa58c7b569962279ce920c6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2172f96f29888f02c6f289836c5f6de01a904cc1f60925aa790d1cdfd6e568d1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPagerdutyIntegration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62646b2686cb0cee153a5821ba8e0df5b17e208f27f57a52031ffb88e1ec21ad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d872ca6f7e72efc4eaf291aa085ceac5730bf943fb8cc9be06a4efcdb9a1bc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14209f5c16a0d4af6b24b0bbc00efa979f1910bf5872c943c589a181ab183176(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee550419c38f6e7eac8ff45bd56e15957d328f3dc2e366610b2c830d127c512e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyPagerdutyIntegration]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__258d023569651f49c9a0ef8754f2acc85563df208a3d211afd6fd16f8cf1d233(
    *,
    id: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b0a7c90f1ac8e2dca016ed7b1ff17bae37497d43e9ec3f1d837701295a78e9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40304512fb180704391335d0cd3945d708438ded21ea118e9c8d7e94fc5c252e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b97787639adff1d793085035bab6454cec45db5d77e23bf26e1540c195039db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90c8e49b57d54d73e8b992c50a3455fd55dc0ecb23cdf1fd52dccda6b80b5162(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7f2d279ae511c82a13f8d8576726900198da9d47e5fc84e86089c6038191319(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00fe6bdd8f487c8357ece56ba834b085434cb1ac17d30d641ebf2de7aba4dc34(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyWebhooksIntegration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09570917e5937ea65e4c6e340e86776ea1f0acfdf7a62c3c2a9c8fc712c9fdc2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3024ecaf47fad063f4cca152ae32ea9e27c96dbd4455ba841f9fdae858639da8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8812fd2040bd87724281811ebced61ba00e5a73bed5cae5c1db3a2a4e1859ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b025e6c9620e926c1b00efb1c1b86166c7e242632537a4552f32266f831ff76(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NotificationPolicyWebhooksIntegration]],
) -> None:
    """Type checking stubs"""
    pass
