from django.contrib import admin

from .. import models


class AccountDomainFilter(admin.SimpleListFilter):
    title = "Local"

    parameter_name = "local"

    def lookups(self, request, model_admin):
        return {("yes", "Yes"), ("no", "No")}

    def queryset(self, request, queryset):
        selection = self.value()

        if selection is None:
            return queryset

        filter_qs = queryset.filter if selection == "yes" else queryset.exclude
        return filter_qs(domain__local=True)


class MessageDirectionFilter(admin.SimpleListFilter):
    title = "Direction"

    parameter_name = "local"

    def lookups(self, request, model_admin):
        return {("incoming", "Incoming"), ("outgoing", "Outgoing")}

    def queryset(self, request, queryset):
        selection = self.value()

        if selection is None:
            return queryset

        filter_qs = queryset.filter if selection == "incoming" else queryset.exclude
        return filter_qs(recipient__domain__local=True)


class MessageVerifiedFilter(admin.SimpleListFilter):
    title = "Verified"

    parameter_name = "verified"

    def lookups(self, request, model_admin):
        return {("yes", "Yes"), ("no", "No")}

    def queryset(self, request, queryset):
        selection = self.value()

        if selection is None:
            return queryset

        filter_qs = queryset.filter if selection == "yes" else queryset.exclude
        return filter_qs(verified=True)


class ActivityTypeFilter(admin.SimpleListFilter):
    title = "Activity Type"

    parameter_name = "activity_type"

    def lookups(self, request, model_admin):
        return models.Activity.Types.choices

    def queryset(self, request, queryset):
        selection = self.value()

        if selection is None:
            return queryset

        return queryset.filter(activity__item__as_activity__type=selection)
