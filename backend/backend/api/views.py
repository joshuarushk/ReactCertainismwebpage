from django.http import JsonResponse
from django.views import View

class CorePrinciplesView(View):
    def get(self, request):
        core_principles = {
            "principles": [
                "Extended Modal Realism: All possible worlds exist concurrently in a vast, interconnected multiverse.",
                "Humean Causality: Causality is a cognitive construct imposed on a causally neutral reality."
            ]
        }
        return JsonResponse(core_principles)

class PropositionsView(View):
    def get(self, request):
        propositions = {
            "propositions": [
                "Proposition 1: There is something, therefore there is something.",
                "Proposition 2: Because something exists, its absence cannot."
            ]
        }
        return JsonResponse(propositions)
