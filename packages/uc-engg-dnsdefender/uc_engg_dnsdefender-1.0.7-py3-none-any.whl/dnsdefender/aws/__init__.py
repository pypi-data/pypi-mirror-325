"""
AWS Module for dnsdefender
"""

from .ec2 import get_ec2_instances
from .lb import get_load_balancers
from .eips import get_eips
from .route53 import get_route53_records

__all__ = ["get_ec2_instances", "get_load_balancers", "get_eips", "get_route53_records"]
