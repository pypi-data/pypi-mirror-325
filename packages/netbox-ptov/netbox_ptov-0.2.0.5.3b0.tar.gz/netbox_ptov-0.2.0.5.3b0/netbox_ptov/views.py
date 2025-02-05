"""Defines the 'views' used by the Django apps for serving pages of the netbox_ptov plugin"""

import django
from ptovnetlab import ptovnetlab as ptvnl
from netbox.views import generic
from netbox_ptov import filtersets, forms, models, tables
from netbox_ptov.models import gns3srv
from django.shortcuts import render, redirect
from django.contrib import messages
import json
import logging


class MessagesHandler(logging.Handler):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def emit(self, record):
        try:
            msg = self.format(record)
            messages.add_message(self.request, messages.INFO, msg)
        except Exception:
            self.handleError(record)



def golab(request: forms.golabForm) -> django.http.HttpResponse:
    """Pass the input fields from the golabForm instance to the ptovnetlab.p_to_v function and return the results as an HttpResponse"""

   # Create a custom logging handler
    messages_handler = MessagesHandler(request)
    messages_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    messages_handler.setFormatter(formatter)

    # Get the logger used by ptovnetlab.p_to_v
    logger = logging.getLogger('ptovnetlab')
    logger.addHandler(messages_handler)


    
    if request.method == 'POST':
        form = forms.golabForm(request.POST)
        if form.is_valid():
            unm = form.cleaned_data['username_in']
            pwd = form.cleaned_data['password_in']
            swl = []
            swl_in = []
            swl_in = form.cleaned_data['switchlist_multiplechoice_in']
            for swname in swl_in:
                print (swname, type(swname))        
                swl.append(str(swname))
            messages.add_message(request, messages.INFO, 'Switch-list: ' + str(swl))
            srv = form.cleaned_data['serverselect_in'].name
            prn = form.cleaned_data['prjname_in']
            # Do something with the text (e.g., save to database)

            messages.add_message(request, messages.INFO, 'GNS3 server: ' + str(srv))



            try:
                    # Call the function that generates logs
                    result_out = str(ptvnl.p_to_v(username=unm, passwd=pwd , servername=srv, switchlist=swl, prjname=prn))
                    messages.add_message(request, messages.SUCCESS, 'Project Created: ' + str(prn) + ' on ' + str(srv))
                    messages.add_message(request, messages.INFO, 'Open project here: <a href='+result_out+' >'+result_out+'</a>' , extra_tags='safe')
            except Exception as e:
                # Handle any exceptions and add an error message
                messages.add_message(request, messages.ERROR, f'An error occurred: {str(e)}')
            finally:
                # Remove the custom handler to avoid duplicate messages in subsequent requests
                logger.removeHandler(messages_handler)
            return render(request, 'golab.html', {'form': form})
    else:
        form = forms.golabForm()
        return render(request, 'golab.html', {'form': form})

class gns3srvView(generic.ObjectView):
    """A class to represent the generic view of a gns3srv object."""

    queryset = models.gns3srv.objects.all()


class gns3srvListView(generic.ObjectListView):
    """A class to represent the view of all gns3srv objects."""

    queryset = models.gns3srv.objects.all()
    table = tables.gns3srvTable


class gns3srvEditView(generic.ObjectEditView):
    """A class to represent the edit view of a gns3srv object.
    =============================================================

    Attributes
    ----------
    queryset
    form
    """
    queryset = models.gns3srv.objects.all()
    form = forms.gns3srvForm


class gns3srvDeleteView(generic.ObjectDeleteView):
    """A class to represent the delete view of a gns3srv object.
    =============================================================
    ...

    Attributes
    ----------
    queryset
    """
    queryset = models.gns3srv.objects.all()


class ptovjobView(generic.ObjectView):
    """
    A class to represent the generic view of all ptovjob objects.

    =============================================================

    Attributes
    ----------
    queryset
    """
    queryset = models.ptovjob.objects.all()


class ptovjobListView(generic.ObjectListView):
    """
    A class to represent the list view of all ptovjob objects.

    =============================================================

    Attributes
    ----------
    queryset
    table
    """
    queryset = models.ptovjob.objects.all()
    table = tables.ptovjobTable


class ptovjobEditView(generic.ObjectEditView):
    """
    A class to represent the edit view of a ptovjob object.

    =============================================================

    Attributes
    ----------
    queryset
    form
    """
    queryset = models.ptovjob.objects.all()
    form = forms.ptovjobForm


class ptovjobDeleteView(generic.ObjectDeleteView):
    """
    A class to represent the delete  view of a ptovjob object.

    =============================================================

    Attributes
    ----------
    queryset
    """

    queryset = models.ptovjob.objects.all()


class switchtojobView(generic.ObjectView):
    """
    A class to represent the generic view of all switchtojob objects.

    =============================================================

    Attributes
    ----------
    queryset
    """
    queryset = models.switchtojob.objects.all()


class switchtojobListView(generic.ObjectListView):
    """
    A class to represent the list view of all switchtojob objects.

    =============================================================

    Attributes
    ----------
    queryset
    table
    """

    queryset = models.switchtojob.objects.all()
    table = tables.switchtojobTable


class switchtojobEditView(generic.ObjectEditView):
    """
    A class to represent the edit view of switchtojob objects.

    =============================================================

    Attributes
    =============================================================
    queryset
    form
    """

    queryset = models.switchtojob.objects.all()
    form = forms.switchtojobForm


class switchtojobDeleteView(generic.ObjectDeleteView):
    """
    A class to represent the delete view of a switchtojob object.

    =============================================================

    Attributes
    ----------
    queryset
    """

    queryset = models.switchtojob.objects.all()
