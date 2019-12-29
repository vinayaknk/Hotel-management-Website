from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView, DeleteView, UpdateView
from . models import Reserve, Roomservice, Meal
from . forms import ReservationForm, RoomServiceForm
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
User = get_user_model()

class ReservePage(LoginRequiredMixin,CreateView):
    template_name = 'reservation/reserve_form.html'
    model = Reserve
    form_class = ReservationForm
    # redirect_field_name = 'reservation/reserve_detail'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ReservePage, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class UpdateReservePage(LoginRequiredMixin,UpdateView):
    template_name = 'reservation/reserve_form.html'
    model = Reserve
    form_class = ReservationForm
    # redirect_field_name = 'reservation/reserve_detail'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(UpdateReservePage, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ReserveDetail(LoginRequiredMixin,DetailView):
    template_name = 'reservation/reserve_detail.html'
    model = Reserve

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(name__username__iexact=self.kwargs.get("username"))

class ReserveDetailAllView(LoginRequiredMixin,DetailView):
    model = Reserve

class UserPosts(LoginRequiredMixin,ListView):
    model = Reserve
    template_name = "reservation/user_reserve_list.html"

    def get_queryset(self):
        try:
            self.reserve_user = User.objects.prefetch_related("reserve").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.reserve_user.reserve.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reserve_user"] = self.reserve_user
        return context

class DeletePost(LoginRequiredMixin,DeleteView):
    model = Reserve
    # select_related = ("user", "group")
    success_url = reverse_lazy("reservation:reserve")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(name_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Reservation Canceled")
        return super().delete(*args, **kwargs)

class RoomserviceView(LoginRequiredMixin,CreateView):
    template_name = 'reservation/roomservice_form.html'
    model = Roomservice
    form_class = RoomServiceForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(RoomserviceView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class MealListView(LoginRequiredMixin,ListView):
    model = Roomservice
    template_name = "reservation/meal_list.html"

    def get_queryset(self):
        return Roomservice.objects.filter(name=self.request.user)
            # prefetch_related("name").get(name__iexact=self.kwargs.get("username"))


    # def get_queryset(self):
    #     try:
    #         self.roomservice_name = Roomservice.objects.prefetch_related("name").get(username__iexact=self.kwargs.get("username"))
    #         print("11111111111 ", self.roomservice_name)
    #     except User.DoesNotExist:
    #         print("2222222222222222")
    #         raise Http404
    #     else:
    #         return self.roomservice_name.roomservice.all()
    #

class DeleteRoomService(LoginRequiredMixin,DeleteView):
    model = Roomservice
    template_name = "reservation/roomservice_confirm_delete.html"
    # success_url = reverse_lazy("reservation:reserve")

    def get_success_url(self):
        return reverse_lazy('reservation:meal_list', kwargs={'username': self.request.user.username})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(name=self.request.user)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Meal Order Canceled")
        return super().delete(*args, **kwargs)

