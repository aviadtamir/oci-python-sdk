# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodePoolCyclingDetails(object):
    """
    Node Pool Cycling Details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodePoolCyclingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param maximum_unavailable:
            The value to assign to the maximum_unavailable property of this NodePoolCyclingDetails.
        :type maximum_unavailable: str

        :param maximum_surge:
            The value to assign to the maximum_surge property of this NodePoolCyclingDetails.
        :type maximum_surge: str

        :param is_node_cycling_enabled:
            The value to assign to the is_node_cycling_enabled property of this NodePoolCyclingDetails.
        :type is_node_cycling_enabled: bool

        """
        self.swagger_types = {
            'maximum_unavailable': 'str',
            'maximum_surge': 'str',
            'is_node_cycling_enabled': 'bool'
        }

        self.attribute_map = {
            'maximum_unavailable': 'maximumUnavailable',
            'maximum_surge': 'maximumSurge',
            'is_node_cycling_enabled': 'isNodeCyclingEnabled'
        }

        self._maximum_unavailable = None
        self._maximum_surge = None
        self._is_node_cycling_enabled = None

    @property
    def maximum_unavailable(self):
        """
        Gets the maximum_unavailable of this NodePoolCyclingDetails.
        Maximum active nodes that would be terminated from nodepool during the cycling nodepool process.
        OKE supports both integer and percentage input.
        Defaults to 0, Ranges from 0 to Nodepool size or 0% to 100%


        :return: The maximum_unavailable of this NodePoolCyclingDetails.
        :rtype: str
        """
        return self._maximum_unavailable

    @maximum_unavailable.setter
    def maximum_unavailable(self, maximum_unavailable):
        """
        Sets the maximum_unavailable of this NodePoolCyclingDetails.
        Maximum active nodes that would be terminated from nodepool during the cycling nodepool process.
        OKE supports both integer and percentage input.
        Defaults to 0, Ranges from 0 to Nodepool size or 0% to 100%


        :param maximum_unavailable: The maximum_unavailable of this NodePoolCyclingDetails.
        :type: str
        """
        self._maximum_unavailable = maximum_unavailable

    @property
    def maximum_surge(self):
        """
        Gets the maximum_surge of this NodePoolCyclingDetails.
        Maximum additional new compute instances that would be temporarily created and added to nodepool during the cycling nodepool process.
        OKE supports both integer and percentage input.
        Defaults to 1, Ranges from 0 to Nodepool size or 0% to 100%


        :return: The maximum_surge of this NodePoolCyclingDetails.
        :rtype: str
        """
        return self._maximum_surge

    @maximum_surge.setter
    def maximum_surge(self, maximum_surge):
        """
        Sets the maximum_surge of this NodePoolCyclingDetails.
        Maximum additional new compute instances that would be temporarily created and added to nodepool during the cycling nodepool process.
        OKE supports both integer and percentage input.
        Defaults to 1, Ranges from 0 to Nodepool size or 0% to 100%


        :param maximum_surge: The maximum_surge of this NodePoolCyclingDetails.
        :type: str
        """
        self._maximum_surge = maximum_surge

    @property
    def is_node_cycling_enabled(self):
        """
        Gets the is_node_cycling_enabled of this NodePoolCyclingDetails.
        If nodes in the nodepool will be cycled to have new changes.


        :return: The is_node_cycling_enabled of this NodePoolCyclingDetails.
        :rtype: bool
        """
        return self._is_node_cycling_enabled

    @is_node_cycling_enabled.setter
    def is_node_cycling_enabled(self, is_node_cycling_enabled):
        """
        Sets the is_node_cycling_enabled of this NodePoolCyclingDetails.
        If nodes in the nodepool will be cycled to have new changes.


        :param is_node_cycling_enabled: The is_node_cycling_enabled of this NodePoolCyclingDetails.
        :type: bool
        """
        self._is_node_cycling_enabled = is_node_cycling_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
