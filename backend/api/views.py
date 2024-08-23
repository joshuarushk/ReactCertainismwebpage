from django.http import JsonResponse
from django.views import View

class CorePrinciplesView(View):
    def get(self, request):
        core_principles = {
            "principles": [
                "Extended Modal Realism: All possible worlds exist concurrently in a vast, interconnected multiverse.",
                "Humean Causality: Causality is a cognitive construct imposed on a causally neutral reality.",
                "Concurrent Existence: Every possible state of being exists simultaneously, without temporal separation.",
                "Illusion of Change: Perceived movement and change are mental constructs; reality is static."
            ]
        }
        return JsonResponse(core_principles)

class FundamentalTenetsView(View):
    def get(self, request):
        fundamental_tenets = {
            "tenets": [
                "Perception and Reality: Our perception is a limited, structured interpretation of a complex reality.",
                "In/Determinism and Free Will: Traditional notions of free will are redefined under concurrent existence.",
                "Epistemology: Knowledge is treated as infallible, where certainty must be incompatible with falsehood."
            ]
        }
        return JsonResponse(fundamental_tenets)

class PropositionsView(View):
    def get(self, request):
        propositions = {
            "propositions": [
                "Proposition 1: There is something, therefore there is something.",
                "Proposition 2: Because something exists, its absence cannot.",
                "Proposition 3: All events and objects have an apparent cause tracing back infinitely.",
                "Proposition 4: Cause and effect are inductive and uncertain; hence, they should be treated as false.",
                "Proposition 5: The foundations of classical logic are anthropomorphic and fallible."
            ]
        }
        return JsonResponse(propositions)

class TheoreticalFoundationsView(View):
    def get(self, request):
        theoretical_foundations = {
            "foundations": [
                "Extended Modal Realism: Possible worlds are not hypothetical but physically real.",
                "Causal Neutrality: Causality is a cognitive imposition rather than an intrinsic property."
            ]
        }
        return JsonResponse(theoretical_foundations)

class PracticalApplicationsView(View):
    def get(self, request):
        practical_applications = {
            "applications": [
                "Scientific Inquiry: Focuses on mapping the interconnections of possible worlds.",
                "Ethics and Morality: Ethical theories must consider the concurrent existence of all possible states.",
                "Personal Identity and Psychology: Recognizing the illusory nature of change impacts self-conception and mental health."
            ]
        }
        return JsonResponse(practical_applications)
