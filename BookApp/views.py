from django.shortcuts import render, redirect
from BookApp.models import UsedBooks, RegisteredUsers
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import pickle, random, numpy

# Required Dataframes
popular_df=pickle.load(open('static/model/popular.pkl','rb'))
final_ratings=pickle.load(open('static/model/final_ratings.pkl','rb'))
pivot_table=pickle.load(open('static/model/pivot_table.pkl','rb'))
similarity_score=pickle.load(open('static/model/similarity_score.pkl','rb'))
books=pickle.load(open('static/model/books.pkl','rb'))

# Required Functions

# get a list with book-titles
book_name_list = list(final_ratings['Book-Title'].str.split().str.join("").str.lower().unique())

def booksearch(usersearch: str):
    # return a list with similar tags
    usersearch = "".join(usersearch.split()).lower()
    tag_search_list = []
    for words in book_name_list:
        if usersearch in words:
            tag_search_list.append(words)

    img_list = []
    title_list = []
    author_list = []
    votes_list = []
    rating_list = []

    if tag_search_list:
        for tag in tag_search_list:
            image = final_ratings.loc[final_ratings['tags'] == tag]['Image-URL-M'].unique()[0]
            title = final_ratings.loc[final_ratings['tags'] == tag]['Book-Title'].unique()[0]
            author = final_ratings.loc[final_ratings['tags'] == tag]['Book-Author'].unique()[0]
            votes = final_ratings.loc[final_ratings['tags'] == tag]['Num_Ratings'].unique()[0]
            rating = final_ratings.loc[final_ratings['tags'] == tag]['Avg_Rating'].unique()[0]

            img_list.append(image)
            title_list.append(title)
            author_list.append(author)
            votes_list.append(votes)
            rating_list.append(rating)

        combined_list = list(zip(img_list, title_list, author_list, votes_list, rating_list))

        return [combined_list, "found"]

    else:
        
        combined_results = []  # Initialize a list to collect results
        for i in range(6):
            random_tag = book_name_list[random.randint(0, len(book_name_list) - 1)]
            # Capture the result of the recursive call and extend the combined_results list.
            combined_results.extend(booksearch(random_tag)[0])
        return [combined_results, "notfound"]

def bookrecommend(book_name:str):
    # get the index no. from pivot_table using index
    index=numpy.where(pivot_table.index==book_name)[0][0]
    # get the list of similar indexes
    similarity_list=sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1], reverse=True)[1:13]
    
    similar_book_img=[]
    similar_book_title=[]
    similar_book_author=[]
    similar_book_votes=[]
    similar_book_rating=[]    

    for index in similarity_list:        
        title=pivot_table.index[index[0]] # get the title from pivot_table using index(similar_list index)
        
        similar_book_img.append(books.loc[books['Book-Title']==title]['Image-URL-L'].drop_duplicates().values[0])
        similar_book_title.append(final_ratings.loc[final_ratings['Book-Title']==title]['Book-Title'].drop_duplicates().values[0])
        similar_book_author.append(final_ratings.loc[final_ratings['Book-Title']==title]['Book-Author'].drop_duplicates().values[0])
        similar_book_votes.append(final_ratings.loc[final_ratings['Book-Title']==title]['Num_Ratings'].drop_duplicates().values[0])
        similar_book_rating.append(final_ratings.loc[final_ratings['Book-Title']==title]['Avg_Rating'].drop_duplicates().values[0])
        
    combined_list=list(zip(similar_book_img,similar_book_title,similar_book_author,similar_book_votes,similar_book_rating))
    return combined_list


# Create your views here.
def index(request):
    
    # fetch UsedBooks details from database
    bookobjs=UsedBooks.objects.all()
    
    return render(request,"index.html",{'ubook':bookobjs})

def register(request):

    if request.method=="POST":
        userfullname=request.POST['userfullname']
        usermobile=request.POST['usermobile']
        useremail=request.POST['useremail']
        username=request.POST['username']
        userpasswd=request.POST['userpasswd']

        if (RegisteredUsers.objects.filter(email=useremail).exists()) or (RegisteredUsers.objects.filter(mobile_no=usermobile).exists()):
            messages.error(request, "User Already Exists!")

            return redirect("/PageTurn")
        
        elif (RegisteredUsers.objects.filter(username=username).exists()):
            messages.warning(request, "User with same Username already Exists!")

            return redirect("/PageTurn")

        else:
            user_data=RegisteredUsers(full_name=userfullname, mobile_no=usermobile, email=useremail, username=username, password=userpasswd)
            
            # Handling Exception if the Email is not Sent
            try:
                subject = 'Welcome to PageTurn'
                message = 'Hi {}, Thank you for registering with PageTurn'.format(username)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [useremail, ]
                send_mail( subject, message, email_from, recipient_list )

            except Exception as error:
                messages.error(request, "Email Not Sent!")
                print(error)

            finally:
                user_data.save()
                messages.success(request, "User Registered Successfully!!")
                return redirect("/PageTurn")

def login(request):

    if request.method=="POST":
        username=request.POST['username']
        userpasswd=request.POST['userpasswd']

        if (RegisteredUsers.objects.filter(username=username,password=userpasswd)):
            messages.success(request, "Login Successful!")

            return render(request, "login.html")
        else:
            messages.warning(request, "User not Found!")

            return render(request, "login.html")
    else:
        return render(request, "login.html")

def whyuse(request):
    return render(request, "whyuse.html")

def mostlybought(request):

    book_name=popular_df['Book-Title'].tolist()
    book_author=popular_df['Book-Author'].tolist()
    book_image=popular_df['Image-URL-M'].tolist()
    book_votes=popular_df['Num_Ratings'].tolist()
    book_rating=popular_df['Avg_Rating'].tolist()

    combined_list=zip(book_name,book_author,book_image,book_votes,book_rating)

    context={'combined_list':combined_list}

    return render(request, "mostlybought.html", context)

def aboutus(request):
    return render(request, "aboutus.html")

def termsconditions(request):
    return render(request, "terms.html")

def privacypolicy(request):
    return render(request, "privacy.html")

def safetytips(request):
    return render(request, "safety.html")

def helpline(request):
    return render(request, "helpline.html")

def sellbooks(request):
    return render(request, "sell.html")

def search(request):
    if request.method=="POST":
        usersearch=request.POST['usersearch']
        search_result=booksearch(str(usersearch))
        
        if search_result[-1]=="notfound":
            messages.error(request, "Book Not Found!")
        
        context={"usersearch":usersearch,# it is passed to store the value in search bar
                "combined_list":search_result[0]                 
                }

    
    return render(request, "booksearch.html", context)

def recommend(request):
    if request.method=="POST":
        selected_img=request.POST['selected_img']
        selected_title=request.POST['selected_title']
        selected_author=request.POST['selected_author']
        selected_votes=request.POST['selected_votes']
        selected_rating=request.POST['selected_rating']
        
        recommend_result=bookrecommend(selected_title)
        
        context={
            "usersearch":selected_title,# search bar will be updated with new value
            "selected_img":selected_img,
            "selected_title":selected_title,
            "selected_author":selected_author,
            "selected_votes":selected_votes,
            "selected_rating":selected_rating,
            "recommend_list":recommend_result}

    return render(request, "recommend.html", context)