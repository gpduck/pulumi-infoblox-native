# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AArgs', 'A']

@pulumi.input_type
class AArgs:
    def __init__(__self__, *,
                 ipv4addr: pulumi.Input[str],
                 name: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 view: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a A resource.
        """
        pulumi.set(__self__, "ipv4addr", ipv4addr)
        pulumi.set(__self__, "name", name)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if view is not None:
            pulumi.set(__self__, "view", view)

    @property
    @pulumi.getter
    def ipv4addr(self) -> pulumi.Input[str]:
        return pulumi.get(self, "ipv4addr")

    @ipv4addr.setter
    def ipv4addr(self, value: pulumi.Input[str]):
        pulumi.set(self, "ipv4addr", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "view")

    @view.setter
    def view(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "view", value)


class A(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 ipv4addr: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 view: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a A resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a A resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 ipv4addr: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 view: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        else:
            opts = copy.copy(opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AArgs.__new__(AArgs)

            __props__.__dict__["comment"] = comment
            if ipv4addr is None and not opts.urn:
                raise TypeError("Missing required property 'ipv4addr'")
            __props__.__dict__["ipv4addr"] = ipv4addr
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["ttl"] = ttl
            __props__.__dict__["view"] = view
        super(A, __self__).__init__(
            'infoblox:record:a',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'A':
        """
        Get an existing A resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AArgs.__new__(AArgs)

        __props__.__dict__["comment"] = None
        __props__.__dict__["ipv4addr"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["ttl"] = None
        __props__.__dict__["view"] = None
        return A(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter
    def ipv4addr(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ipv4addr")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def view(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "view")

