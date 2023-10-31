from .models import Sing, Contact, Log ,LostItem1 , FoundItem ,PostNews ,Category,Item,Bid
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .forms import LostItemForm
from .forms import FoundItemForm
from .models import LostItem1, FoundItem
from .forms import PostNewsForm
from .forms import PostCategoryForm
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import RegistrationForm, Login_Form
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .forms import BidForm
from .models import Bid, MyCustomUsers
from .models import BiddingItem
from .forms import BidUpdateForm



# Create your views here.
def index(request):
    return render(request, 'index.html')

def Aboutus(request):
    return render(request,'Aboutus.html')

def Contactus(request):
    if request.method == 'POST':
        # Process the form data here
        uu_id = request.POST.get('uu_id')
        contact_date = request.POST.get('contact_date')
        subject = request.POST.get('subject')
        
        # Save the form data or perform any desired actions
        
        return redirect('thankyou_url')  # Redirect to the thank you page
    
    return render(request, 'contactus.html') 

def thankyou(request):
  return render(request, 'Thanks.html')   


def login_view(request):
    form = Login_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            if user is not None:
                login(request, user)
                return redirect('user_dashboard')
            else:
                messages.error(request, 'Invalid Password or Email')
    return render(request, 'login.html', {'form': form})


def user_dashboard(request):
    lost_items = LostItem1.objects.all()
    found_items = FoundItem.objects.all()
    lost_item_count = lost_items.count()
    found_item_count = found_items.count()
    return render(request, 'User/UserDashBoard.html', {'lost_item_count': lost_item_count, 'found_item_count': found_item_count})
    
def user_page(request):
    username = request.user.username
    return render(request, 'User/user_page.html', {'username': username}) 


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index_url')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def admin_view(request):
    # Add your logic for the admin page here
    # ...
    return render(request, 'admin_page.html')


def Anno(request):
    return render(request,'User/UserAnno.html') 


def UserLostAndFound(request):
    lost_form = LostItem1.objects.all()  # Fetch all lost items from the database
    found_item = FoundItem.objects.all()  # Fetch all found items from the database
    return render(request, 'User/UserLostAndFound.html', {'lost_form': lost_form, 'found_item': found_item})
      

def UserHelp(request):
    return render(request,'User/UserHelp.html') 

def UserReports(request):
    
    return render(request,'User/UserReports.html')  


def lost_form(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Successfully Added!')
            return redirect('UserReports')  # Redirect to a success page
    else:
        form = LostItemForm()
        messages.error(request, "You must be an administrator to perform this action.")
        return render(request, 'User/lostForm.html')

    return render(request, 'User/lostForm.html', {'form': form})


def Help(request):
    return render(request,'User/Help.html')  


def found_item(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added! ')
            return redirect('UserReports')  # Redirect to a success page
    else:
        form = FoundItemForm()
        messages.error(request, "You must be an administrator to perform this action.")
        return render(request, 'User/foundForm.html')
    
    return render(request, 'User/foundForm.html', {'form': form})
   


def biddingpage(request):
 
    adminManageBid=Item.objects.filter().first()
    approve_bid=Bid.objects.all()
    context = {
            'adminManageBid':adminManageBid,
            'approve_bid':approve_bid,
            'bid_id': adminManageBid.id
    }
    
    return render(request,'User/biddingpage.html', context)



#######ADMIN PAGE

def login_admin(request):
    return render(request, 'Logine.html')

def dashboard_admin(request):
    return render(request, 'admin/AdminDashBoard.html')

def AdminLostAndFound(request):
    lost_forms = LostItem1.objects.all()  # Fetch all lost items from the database
    found_items = FoundItem.objects.all()  # Fetch all found items from the database
    context = {
            'lost_forms':lost_forms,
            'found_items':found_items
    }   

    return render(request, 'admin/AdminLostAndFound.html', context)


from django.http import HttpResponse, HttpResponseNotFound

def delete_row(request, item_id):
    try:
        item = LostItem1.objects.get(id=item_id)
        item.delete()
        return HttpResponse("Row deleted successfully")
    except LostItem1.DoesNotExist:
        return HttpResponseNotFound("Row not found")


def found_delete_row(request, item_id):
    try:
        item =FoundItem.objects.get(id=item_id)
        item.delete()
        return HttpResponse("Row deleted successfully")
    except LostItem1.DoesNotExist:
        return HttpResponseNotFound("Row not found")



def edit_post_news(request, post_news_id):
    if request.method == 'POST':
        # Retrieve the edited data from the form
        title = request.POST['title']
        description = request.POST['description']
        addressed_to = request.POST['addressed_to']
        # Update the corresponding AdminPostNews object
        post_news = PostNews.objects.get(id=post_news_id)
        post_news.title = title
        post_news.description = description
        post_news.addressed_to = addressed_to
        post_news.save()
        # Redirect to the desired page or show a success message
        messages.success(request, 'Post news updated successfully.')
        return redirect('AdminManageNews')  # Replace 'post_news_list' with your actual URL name

    else:
        # Retrieve the AdminPostNews object to be edited
        post_news = PostNews.objects.get(id=post_news_id)
        context = {'post_news': post_news}
    return render(request, 'admin/edit_post_news.html', context)


from django.http import JsonResponse

def delete_post_news(request, post_news_id):
    if request.method == 'DELETE':
        # Delete the corresponding AdminPostNews object
        post_news = get_object_or_404(PostNews, id=post_news_id)
        post_news.delete()
        # Return a JSON response to indicate successful deletion
        return JsonResponse({'message': 'Post news deleted successfully.'})
    else:
        # Return a JSON response with an error message if the request method is not DELETE
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def delete_item_bid(request, bid_id):
    if request.method == 'DELETE':
        # Delete the corresponding AdminPostNews object
        post_news = get_object_or_404(Item, id=bid_id)
        post_news.delete()
        # Return a JSON response to indicate successful deletion
        return JsonResponse({'message': 'Post news deleted successfully.'})
    else:
        # Return a JSON response with an error message if the request method is not DELETE
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

def delete_user_bid(request, sing_id):
   
    if request.method == 'DELETE':
        # Delete the corresponding AdminPostNews object
        post_news = get_object_or_404(Sing, id=sing_id)
        post_news.delete()
        # Return a JSON response to indicate successful deletion
        return JsonResponse({'message': 'Post news deleted successfully.'})
    else:
        # Return a JSON response with an error message if the request method is not DELETE
        return JsonResponse({'error': 'Invalid request method.'}, status=400)       



def AdminlostForm(request):
    return render(request, 'admin/AdminlostForm.html')  






def AdminManageBid(request):
    if request.method == 'POST':
        # Get the data from the request
        item_id = request.POST.get('item_id')
        message = request.POST.get('message')

        # Retrieve the item
        item = Item.objects.get(id=item_id)

        # Post to Telegram
        send_message_to_telegram(message)

        # Render the template
        AdminPostItemBidding = Item.objects.all()
        context = {
            'AdminPostItemBidding': AdminPostItemBidding
        }
        
        return render(request, 'admin/AdminManageBid.html', context)
    else:
        AdminPostItemBidding = Item.objects.all()
        context = {
            'AdminPostItemBidding': AdminPostItemBidding
        }
        return render(request, 'admin/AdminManageBid.html', context)


def AdminManageCategory(request):
    return render(request, 'admin/AdminManageCategory.html')

def AdminManageNews(request):
    AdminPostNews = PostNews.objects.all() 
    return render(request, 'admin/AdminManageNews.html',{'AdminPostNews':AdminPostNews})  


from .forms import ItemForm


from django.contrib import messages
from .forms import ItemForm

import requests

def send_telegram_message(message):
    bot_token = '6316874111:AAE0G8HfH1nQfgRXsHXlijn3JAQpx0uDM90'
    chat_id = '-1001832802081'

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Message sent successfully.')
    else:
        print('Failed to send message. Error:', response.text)

def AdminPostItemBidding(request):
    form = ItemForm(request.POST or None, request.FILES or None) 
    if request.method == 'POST':
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Successfully Added! ')
            
            # Prepare the message to be sent to the Telegram channel
            item_details = f"New Item Posted:\n\nTitle: {item.selling_item}\nBid date: {item.bid_date}\nPrice: {item.bid_amount}"
            
            # Send the message to the Telegram channel
            send_telegram_message(item_details)
         
            return redirect('AdminManageBid')
        else:
            messages.error(request, "You must be an administrator to perform this action.")
            return redirect('AdminPostItemBidding')  

    return render(request, 'admin/AdminPostItemBidding.html', {'form': form})

       
def AdminPostNews(request):
    if request.method == 'POST':
        form = PostNewsForm(request.POST)
        if form.is_valid():
            post_news = form.save()
            messages.success(request, 'News posted successfully.')
            return redirect('AdminManageNews')
        else:
            messages.error(request, 'Failed to post the news. Please check the form inputs.')
    else:
        form = PostNewsForm()
    
    return render(request, 'admin/AdminPostNews.html', {'form': form})
    


def AdminUserManagement(request):
    register_view=Sing.objects.all()
    context = {'register_view': register_view}

    return render(request, 'admin/AdminUserManagement.html',context)

def AdminClaimedItems(request):
    return render(request,'admin/AdminClaimedItems.html')

from django.shortcuts import render, redirect
from .models import Bid, BiddingItem
from .forms import BidUpdateForm
from django.contrib import messages

def approve_bid(request):
    bid = Bid.objects.first()
    current_price = bid.price

    form = BidUpdateForm()  # Initialize the form

    if request.method == 'POST':
        form = BidUpdateForm(request.POST)
        if form.is_valid():
            bid_id = form.cleaned_data['bid_id']
            bid_amount = form.cleaned_data['bid_amount']
            try:
                bidding_item = BiddingItem.objects.get(id=bid_id)
                bidding_item.bid_amount = bid_amount
                bidding_item.save()
                messages.success(request, 'The bid has been updated successfully.')
                return redirect('admin_dashboard')
            except BiddingItem.DoesNotExist:
                messages.error(request, 'Invalid bid ID.')
        else:
            messages.error(request, 'Invalid form data.')

    return render(request, 'admin/AdminAprove.html', {'form': form, 'current_price': current_price})

def post_category(request):
    if request.method == 'POST':
        form = PostCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('AdminManageCategory')  # Redirect to the dashboard or another URL
    else:
        form = PostCategoryForm()
    
    return render(request, 'admin/AdminPostNews.html', {'form': form})

  # assuming you're passing the id of the item to be updated

def  update_lost_item(request, item_id):
    item = get_object_or_404(LostItem1, id=item_id)
    if request.method == 'POST':
        # Retrieve the updated data from the form
        # Update the corresponding fields of the item object
        item.location = request.POST['location']
        item.date = request.POST['date']
        item.pd = request.POST['pd']
        item.reward = request.POST['reward']
        item.save()
        # Redirect to the appropriate view
        return redirect('lost_things')
    else:
        return render(request, 'update_lost_item.html', {'item': item})

def delete_lost_item(request, item_id):
    item = get_object_or_404(LostItem1, id=item_id)
    if request.method == 'POST':
        item.delete()
        # Redirect to the appropriate view
        return redirect('lost_things')
    else:
        return render(request, 'delete_lost_item.html', {'item': item})       

def update_found_item(request, item_id):
    item = get_object_or_404(FoundItem, id=item_id)
    if request.method == 'POST':
        # Retrieve the updated data from the form
        location = request.POST.get('location')
        date = request.POST.get('date')
        pd = request.POST.get('pd')

        # Update the corresponding fields of the item object
        item.location = location
        item.date = date
        item.pd = pd
        item.save()
        
        # Redirect to the appropriate view
        return redirect('found_things')
    else:
        return render(request, 'update_found_item.html', {'item': item})

def delete_found_item(request, item_id):
    item = get_object_or_404(FoundItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        # Redirect to the appropriate view
        return redirect('found_things')
    else:
        return render(request, 'delete_found_item.html', {'item': item})

def logout_view(request):
    logout(request)
    return redirect('index_url')  # Redirect to the login page after logout

def admin_page(request):
    username = request.user.username
    return render(request, 'admin/admin_page.html',{'username': username})  
    
def bid_form(request):
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            new_price = form.cleaned_data['newprice']
            bid = Bid(price=new_price)
            bid.save()
            return redirect('Anno')
    else:
        form = BidForm()
    return render(request, 'User/biddingpage.html', {'form': form})