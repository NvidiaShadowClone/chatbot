from rapidfuzz import process, fuzz

# FAQ dictionary with {{cta}} marker where buttons should appear
faq = {
    # Clinic hours
    "what are your clinic hours": "Our clinic is open Monday to Friday from 8am to 6pm, and Saturdays from 9am to 1pm.",
    "clinic open hours": "Our clinic is open Monday to Friday from 8am to 6pm, and Saturdays from 9am to 1pm.",
    "when do you open clinic": "Our clinic is open Monday to Friday from 8am to 6pm, and Saturdays from 9am to 1pm.",
    "what is clinic time/hours": "Our clinic is open Monday to Friday from 8am to 6pm, and Saturdays from 9am to 1pm.",
    "what time does the clinic open": "Our clinic is open Monday to Friday from 8am to 6pm, and Saturdays from 9am to 1pm.",
    "what time do you close": "Our clinic is open Monday to Friday from 8am to 6pm, and Saturdays from 9am to 1pm.",
    "clinic timings": "Our clinic is open Monday to Friday from 8am to 6pm, and Saturdays from 9am to 1pm.",
    "operating hours of clinic": "Our clinic is open Monday to Friday from 8am to 6pm, and Saturdays from 9am to 1pm.",
    "hours of operation": "Our clinic is open Monday to Friday from 8am to 6pm, and Saturdays from 9am to 1pm.",
    "clinic working hours": "Our clinic is open Monday to Friday from 8am to 6pm, and Saturdays from 9am to 1pm.",


    # Booking and scheduling
    "how can i book an appointment": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "book an appointment": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "schedule appointment": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "book now": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "i want to book now": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "how do i book now": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "make an appointment": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "schedule a session": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "book a session": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "appointment booking": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "how do i schedule an appointment": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "how do i make an appointment": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "i need an appointment": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "can i book a session online": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "can you help me book": "You can book an appointment by calling us at (123) 456-7890 or through our online booking system. {{cta}}",
    "i need to schedule": "You can schedule by calling us at (123) 456-7890 or through our online system. {{cta}}",
    "need help booking appointment": "You can schedule by calling us at (123) 456-7890 or through our online system. {{cta}}",

    # Phone call or meeting
    "book a call": "To book a call, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "schedule a call": "To book a call, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "book a consultation": "To book a consultation, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "schedule consultation": "To book a consultation, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "i want to book a call": "To book a call, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "how can i book a call": "To book a call, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "book a meeting": "To book a meeting, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "schedule a meeting": "To book a meeting, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "book me a call": "To book a call, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "can i book a call": "To book a call, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "how to book a consultation call": "To book a consultation, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "need to speak with someone": "To book a call, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "how do i talk to a physiotherapist": "To book a consultation, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "want to speak with therapist": "To book a call, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",
    "request a consultation": "To book a consultation, please call us at (123) 456-7890 or use our online scheduler. {{cta}}",

    # conditions treated
    "what injuries do you handle": "We treat a variety of conditions including sports injuries, back pain, arthritis, post-surgery rehabilitation, and more.",
    "what do you specialize in": "We treat a variety of conditions including sports injuries, back pain, arthritis, post-surgery rehabilitation, and more.",
    "what can you help me with": "We treat a variety of conditions including sports injuries, back pain, arthritis, post-surgery rehabilitation, and more.",
    "do you treat back pain": "We treat a variety of conditions including sports injuries, back pain, arthritis, post-surgery rehabilitation, and more.",
    "do you help with arthritis": "We treat a variety of conditions including sports injuries, back pain, arthritis, post-surgery rehabilitation, and more.",

    # insurance
    "can i use insurance": "Yes, we accept most major insurance plans. Please check with your provider to confirm coverage.",
    "do you do insurance claims": "Yes, we accept most major insurance plans. Please check with your provider to confirm coverage.",
    "is insurance accepted": "Yes, we accept most major insurance plans. Please check with your provider to confirm coverage.",
    "how does insurance work": "Yes, we accept most major insurance plans. Please check with your provider to confirm coverage.",
    "do you do direct insurance billing": "Yes, we offer direct billing for many insurance providers to simplify payment.",


    # General scheduling intent
    "how do i schedule": "You can schedule by calling us at (123) 456-7890 or through our online system. {{cta}}",
    "help me schedule an appointment": "You can schedule by calling us at (123) 456-7890 or through our online system. {{cta}}",
    "need to book an appointment": "You can schedule by calling us at (123) 456-7890 or through our online system. {{cta}}",
    "want to schedule an appointment": "You can schedule by calling us at (123) 456-7890 or through our online system. {{cta}}",
    "is referral required for physiotherapy": "No referral is necessary. You can book an appointment directly with us.",
    "do i have to get referred": "No referral is necessary. You can book an appointment directly with us.",
    "can i come without referral": "No referral is necessary. You can book an appointment directly with us.",
    "do you need doctor referral": "No referral is necessary. You can book an appointment directly with us.",

    # clinic location 
    "where is your clinic located": "Our clinic is located at 123 Main Street, Springfield. Parking is available.",
    "clinic address": "Our clinic is located at 123 Main Street, Springfield. Parking is available.",
    "how do i get to your clinic": "Our clinic is located at 123 Main Street, Springfield. Parking is available.",
    "location of the clinic": "Our clinic is located at 123 Main Street, Springfield. Parking is available.",
    "how do i find your clinic": "Our clinic is located at 123 Main Street, Springfield. Parking is available.",

    # emergency
    "do you take emergency appointments": "We try to accommodate urgent cases. Please call us at (123) 456-7890 for immediate assistance.",
    "can i get a same day appointment": "Same day appointments may be available. Please call us at (123) 456-7890 to check availability.",
    "urgent care physiotherapy": "We try to accommodate urgent cases. Please call us at (123) 456-7890 for immediate assistance.",
    "do you accept walk-ins": "We recommend booking in advance, but we may be able to take walk-ins depending on availability. Please call ahead.",

    # Aftercare
    "do i need follow up appointments": "Follow-up sessions are often recommended depending on your condition. Your therapist will guide you.",
    "what happens after my session": "After your session, your physiotherapist may assign exercises or suggest further appointments.",
    "will i get exercises to do at home": "Yes, customized home exercise programs are provided to support your recovery.",

    # payment
    "how can i pay": "We accept Visa, MasterCard, American Express, and PayPal.",
    "what are accepted payments": "We accept Visa, MasterCard, American Express, and PayPal.",
    "can i pay by card": "We accept Visa, MasterCard, American Express, and PayPal.",
    "do you take credit cards": "We accept Visa, MasterCard, American Express, and PayPal.",
    "do you accept paypal": "We accept Visa, MasterCard, American Express, and PayPal.",


    # Other FAQs (non-CTA)
    "do I need a referral to see a physiotherapist": "No referral is necessary. You can book an appointment directly with us.",
    "what payment methods do you accept": "We accept Visa, MasterCard, American Express, and PayPal.",
    "what conditions do you treat": "We treat a variety of conditions including sports injuries, back pain, arthritis, post-surgery rehabilitation, and more.",
    "do you accept insurance": "Yes, we accept most major insurance plans. Please check with your provider to confirm coverage.",
    "how long is a typical session": "Each physiotherapy session typically lasts between 45 minutes to an hour.",
    "what should I bring to my first appointment": "Please bring any relevant medical records, your insurance card, and comfortable clothing suitable for exercise.",
    "do you offer virtual physiotherapy sessions": "Yes, we offer virtual consultations and therapy sessions via video call.",
    "how many sessions will I need": "The number of sessions varies depending on your condition. Your physiotherapist will create a personalized plan.",
    "do you provide home exercise programs": "Yes, customized home exercise programs are provided to support your recovery.",
    "what should I expect during my first visit": "Your physiotherapist will perform an assessment, discuss your goals, and create a treatment plan.",
    "are your physiotherapists licensed": "All our physiotherapists are fully licensed and registered with the appropriate regulatory bodies.",
    "do you treat children and seniors": "Yes, we provide physiotherapy services for patients of all ages.",
    "can physiotherapy help with chronic pain": "Physiotherapy can help manage and reduce chronic pain through targeted treatments.",
    "do you offer massage therapy": "Yes, massage therapy is available as part of our treatment options.",
    "how much does a session cost": "Session costs vary depending on treatment type. Please contact us for detailed pricing.",
    "do you offer direct billing to insurance": "Yes, we offer direct billing for many insurance providers to simplify payment.",
    "can I get physiotherapy after surgery": "Absolutely, post-surgical rehabilitation is a common and important part of recovery.",
    "do you treat sports injuries": "Yes, we specialize in treating a wide range of sports injuries.",
    "what types of physiotherapy techniques do you use": "Our therapists use techniques such as manual therapy, exercise therapy, electrotherapy, and more.",
    "how do I cancel or reschedule an appointment": "Please call us at least 24 hours in advance to cancel or reschedule your appointment.",
    "is parking available at the clinic": "Yes, free parking is available for all our patients.",
    "do you offer weekend appointments": "We offer limited weekend appointments. Please contact us to check availability.",
    "can physiotherapy improve mobility": "Yes, physiotherapy is designed to improve mobility, strength, and function.",
    "do you provide ergonomic assessments": "Yes, we offer workplace ergonomic assessments to help prevent injuries.",
    "what is the difference between physiotherapy and chiropractic care": "Physiotherapy focuses on rehabilitation and exercise, while chiropractic care focuses on spinal adjustments.",
    "how do I know if physiotherapy is right for me": "If you have pain, limited mobility, or an injury, physiotherapy can likely help. Consult with us for an assessment.",
    "do you offer injury prevention programs": "Yes, we offer customized injury prevention programs for athletes and workers.",
    "are there any conditions physiotherapy cannot treat": "While physiotherapy can help many conditions, some complex medical issues may require specialist care.",
    "how soon can I start physiotherapy after an injury": "You can typically start within days of injury, but your physiotherapist will advise based on your specific case."
}

def get_answer(user_question: str) -> str | None:
    # Fuzzy match the question to FAQ keys
    best_match = process.extractOne(
        user_question.lower(),
        faq.keys(),
        scorer=fuzz.ratio,
        score_cutoff=55  # Adjustable match threshold
    )
    if best_match:
        matched_question = best_match[0]
        return faq[matched_question]
    return None
