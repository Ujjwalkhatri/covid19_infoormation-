from django.shortcuts import render,HttpResponse

# Create your views here.
def index (request):
    return HttpResponse ("THIS IS HOME PAGE ABOUT CORONA VIRUS IF YOU WANT THE FURTHER DETAIL PRESS, /ABOUT FOR DISEASE /SYMPTOMS FOR THE REMENDY OF DISEASES ,  /PROTECTION FOR THE PROTECTIVE MEASURES,  /EFFECTS ABOUT HOW THIS DISEASE CAN AFFECT HTE HEALTH ")

def about(request):
    return HttpResponse("Coronaviruses are a group of related RNA viruses that cause diseases in mammals and birds. In humans and birds, they cause respiratory tract infections that can range from mild to lethal. Mild illnesses in humans include some cases of the common cold (which is also caused by other viruses, predominantly rhinoviruses), while more lethal varieties can cause SARS, MERS, and COVID-19. In cows and pigs they cause diarrhea, while in mice they cause hepatitis and encephalomyelitis. There are as yet no vaccines or antiviral drugs to prevent or treat human coronavirus infections. ")

def symptoms (request):
    return HttpResponse("The symptoms of this virus is continous high fever within 14 days, followed by sneezing,neckpaining and difficulty in breathing")    

def protection (request):
    return HttpResponse("The protective measure is wearing mask, staying home , stay away from effected people , as we know this virus sprad too fastly throug contacts , So avoiding high populated area , keeping hydrated , wearing protective gear, washing hand frequently are the protective measures.")

def effect (request):
    return HttpResponse("Covid19 creates severe effects in our health, it can easily deastroy the respiratory organ causing to death. It is extremely fatal diseases, with high mortality rate.")