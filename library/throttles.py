from rest_framework.throttling import UserRateThrottle


class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'


class SustainedRateThrottle(UserRateThrottle):
    scope = 'sustained'


class AverageRateThrottle(UserRateThrottle):
    scope = 'average'


class SlowRateThrottle(UserRateThrottle):
    scope = 'slow'
