from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission


class IsOwner(BasePermission):
    """
      Faqatgina ma'lumotni egalari ko‘rishi va editd qilishi mumkin.
    """

    def has_object_permission(self, request, view, obj):

        return obj.owner == request.user
