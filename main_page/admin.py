from django.contrib import admin
from main_page.models import Slider, Baner, Advantages, Contacts, ContactUs, Subscription, Review


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_editable = ['title', 'position', 'image', 'is_visible', 'h_1', 'desc', 'tab', 'tab_url']
    list_display = ['title', 'position', 'image', 'is_visible', 'h_1', 'desc', 'tab', 'tab_url']
    list_display_links = None


@admin.register(Baner)
class BanerAdmin(admin.ModelAdmin):
    model = Baner
    list_editable = ['title', 'position', 'image_1', 'h_1', 'desc_1', 'tab_1', 'tab_url_1', 'image_2', 'h_2', 'desc_2', 'tab_2', 'tab_url_2',
                     'image_3', 'h_3', 'desc_3', 'tab_3', 'tab_url_3', 'image_4', 'h_4', 'desc_4', 'tab_4', 'tab_url_4']
    list_display = ['title', 'position', 'image_1', 'h_1', 'desc_1', 'tab_1', 'tab_url_1', 'image_2', 'h_2', 'desc_2', 'tab_2', 'tab_url_2',
                    'image_3', 'h_3', 'desc_3', 'tab_3', 'tab_url_3', 'image_4', 'h_4', 'desc_4', 'tab_4', 'tab_url_4']
    list_display_links = None


@admin.register(Advantages)
class AdvantagesAdmin(admin.ModelAdmin):
    model = Advantages
    list_editable = ['title', 'position', 'h_1', 'h_2', 'h_3', 'h_4']
    list_display = ['title', 'position', 'h_1', 'h_2', 'h_3', 'h_4']
    list_display_links = None



@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    model = Contacts
    list_editable = ['address', 'phone_1', 'phone_2', 'phone_3', 'email', 'day_open', 'hours_of_work', 'weekend_work',
                     'weekend_hours_of_work', 'fb_url', 'youtube_url', 'in_url']
    list_display = ['address', 'phone_1', 'phone_2', 'phone_3', 'email', 'day_open', 'hours_of_work', 'weekend_work',
                    'weekend_hours_of_work', 'fb_url', 'youtube_url', 'in_url']
    list_display_links = None


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_editable = ['email', 'is_processed']
    list_display = ['email', 'date', 'date_processing', 'is_processed']
    list_display_links = None


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_editable = ['name', 'email', 'subject', 'message', 'is_processed']
    list_display = ['name', 'email', 'subject', 'message', 'date', 'date_processing', 'is_processed']
    list_display_links = None


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_editable = ['email', 'message', 'rating', 'product', 'date', 'is_approved']
    list_display = ['name', 'email', 'message', 'rating', 'product', 'date', 'is_approved']

