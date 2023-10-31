from django.urls import path, include
from.import views
from .views import index,Aboutus,Contactus ,register_view , login_admin, dashboard_admin , user_dashboard , login_view, Anno ,UserLostAndFound ,UserHelp, UserReports ,lost_form ,Help , found_item ,admin_view ,biddingpage , thankyou ,AdminLostAndFound ,AdminlostForm ,AdminManageBid,AdminManageCategory ,AdminManageNews ,AdminPostItemBidding ,AdminPostNews, AdminUserManagement ,AdminClaimedItems,approve_bid,post_category,user_page,logout_view,admin_page, update_lost_item,delete_lost_item ,update_found_item,delete_found_item,bid_form
urlpatterns = [
   
  path('', index, name="index_url"),
  path('us/',Aboutus, name='Aboutus_url'),
  path('cont/',Contactus, name='Contactus_url'),
  path('register/', register_view, name='register_view'),
  path('admin_new/', login_admin, name='index_admin'),
  path('userdashboard/', user_dashboard, name='user_dashboard'),
  path('login/', login_view, name='login_view'),
  path('Anno/', Anno,name='Anno'),
  path('UserLost/',UserLostAndFound, name='UserLostAndFound'),
  path('UHelp/',UserHelp , name='UserHelp'),
  path('UReports/', UserReports , name='UserReports'),
  path('LForm/',lost_form, name='lost_form'),
  path('useHelp/',Help, name='Help'),
  path('FForm/', found_item, name='found_item'),
  path('admin_view/', admin_view, name='admin_view'),
  path('biddingpage/',biddingpage,name='biddingpage'),
  path('thankyou/',thankyou,name='thankyou_url'),
  path('Uuser_page/',user_page,name='user_page'),
  path('logout/', logout_view, name='logout_view'),

  #admin url
  path('admin_dashboard/', dashboard_admin, name='admin_dashboard'),
  path('AdminLostAndFound/',AdminLostAndFound, name='AdminLostAndFound'),
  path('AlostForm/',AdminlostForm, name='AdminlostForm'),
  path('AManageBid/',AdminManageBid, name='AdminManageBid'),
  path('AManageCategory/',AdminManageCategory, name='AdminManageCategory'),
  path('AManageNews/',AdminManageNews, name='AdminManageNews'),
  path('APostItemBidding/',AdminPostItemBidding , name='AdminPostItemBidding'),
  path('APostNews/',AdminPostNews, name='AdminPostNews'),
  path('AUserManagement/',AdminUserManagement, name='AdminUserManagement'),
  path('AClaimedItems/',AdminClaimedItems, name='AdminClaimedItems'),
  path('Aapprove_bid/',approve_bid, name='approve_bid'),
  path('APostCategory/',post_category, name='post_category'),
  #path('Aupdata/',update, name='update'),
  #path('update/<int:item_id> /', views.update, name='update'),
  path('Aadmin_page/',admin_page,name='admin_page'),
  path('lost_things/update/<int:item_id>/', views.update_lost_item, name='update_lost_item'),
  path('lost_things/delete/<int:item_id>/', views.delete_lost_item, name='delete_lost_item'),
  path('delete-row/<int:item_id>/', views.delete_row, name='delete_row'),
  path('found-delete-row/<int:item_id>/', views.found_delete_row, name='delete_row'),
  path('delete-post-news/<int:post_news_id>/', views.delete_post_news, name='delete_post_news'),
  path('delete_item_bid/<int:bid_id>/', views.delete_item_bid, name='delete_item_bid'),
  path('delete_user_bid/<int:sing_id>/', views.delete_user_bid, name='delete_user_bid'),
    # Other URL patterns...
  path('found_things/update/<int:item_id>/', views.update_found_item, name='update_found_item'),
  path('found_things/delete/<int:item_id>/', views.delete_found_item, name='delete_found_item'),
  path('Ubid_form',bid_form,name='bid_form'),
  path('post-news/edit/<int:post_news_id>/', views.edit_post_news, name='edit_post_news'),
  path('post-news/delete/<int:post_news_id>/', views.delete_post_news, name='delete_post_news'),
  


   
  
   ]


 
 