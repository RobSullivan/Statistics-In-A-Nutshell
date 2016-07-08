


class Probability():
	
	
	def conditional_probability(self, probablity_event_f, probablity_event_e):
		# P(E|F)
		# the probability of some event, given that another event has occurred
		# second event is known as the condition
		# 
		print(probablity_event_f/probablity_event_e)
		return probablity_event_f/probablity_event_e

	
	def intersection_of_independent_events(self, probablity_event_e, probablity_event_f):
		# P(E ∩ F) = P(E) × P(F)
		
		return probablity_event_e * probablity_event_f
	
	def intersection_of_nonindependent_events(self, probablity_event_e, conditional_probability):
		# P(E ∩ F) = P(E) × P(F|E)
		return probablity_event_e * conditional_probability
		
	
	
	def mutually_exclusive_events(self, probablity_event_e, probablity_event_f):
		# P (E ∪ F) = P(E) + P(F)
		return probablity_event_e + probablity_event_f
	
	def not_mutally_exclusive_events(self, probablity_event_e, probablity_event_f):
		# P(E ∪ F) = P(E) + P(F) − P(E ∩ F)
		intersection = self.intersection_of_independent_events(probablity_event_e, probablity_event_f)
		
		union_of_e_and_f = probablity_event_e + probablity_event_f - intersection
		return union_of_e_and_f 
		


probability = Probability()


# Union of mutually exclusive events
probability_english_major = 0.2
probability_french_major = 0.1
result = probability.mutually_exclusive_events(probability_english_major, probability_french_major)
print("Probablity of the event a student is English major or French major is: ", float("{0:.2f}".format(result)))
print()
print()


#Union of events that are not mutually exclusive
result_not_mutex = probability.not_mutally_exclusive_events(probability_english_major, probability_french_major)
print("A college that allows student to take double major: ", float(result_not_mutex))
print()
print()

#Intersection of independent events
probability_of_heads = 0.5
probability_of_tails = 0.5
coin_flip_result = probability.intersection_of_independent_events(probability_of_heads, probability_of_heads)
print("Heads on both flips: ", coin_flip_result)
print()
print()

#INTERSECTION OF NONINDEPENDENT EVENTS
first_black_card = 0.5
conditional_second_black_card_prob = 0.49
two_black_cards_result = probability.intersection_of_nonindependent_events(first_black_card, conditional_second_black_card_prob)
print("probability of drawing two black cards", two_black_cards_result)
