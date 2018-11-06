from rest_framework.permissions import  BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this obj'
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return obj.user == request.user

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

    # def has_permission(self, request, view):
    #     ip_addr = request.META['REMOTE_ADDR']
    #     blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
    #     return not blacklisted
