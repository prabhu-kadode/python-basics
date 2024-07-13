class Voting:
    def __init__(self, candidateList):
        self.title = 'Hi Voting'
        self.totalVote = 0
        self.voteList = []
        self.candidateList = candidateList
        print('Voting started....')

    def startVoting(self, voter):
        result = self.checkEligibility(voter['age'])
        if result:
            self.totalVote += 1
            self.voteList.append(voter)
            self.voteYourCandidate(voter['votingFor'])
        else:
            print("You are not allowed to vote")

    def checkEligibility(self, age):
        return age >= 18

    def voteYourCandidate(self, votingFor):
        for item in self.candidateList:
            if item['party'] == votingFor:
                item['total'] += 1
                break

    def showVictory(self):
        for item in self.candidateList:
            print(item)
        
        partyOne, partyTwo = self.candidateList[0], self.candidateList[1]
        if partyOne['total'] > partyTwo['total']:
            self.showDetails(partyOne)
        else:
            self.showDetails(partyTwo)

    def showDetails(self, party):
        print('===============================')
        print(f"{party['name']} has won successfully")
        print(f"Party: {party['party']}")
        print(f"Total Votes: {party['total']} out of {self.totalVote}")
        print('===============================')
    def showIngrapgh(self):
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        party = []
        counts = []
        bar_labels = []
        for item in self.candidateList:
            party.append(item['party'])
            counts.append(item['total'])
        
        bar_labels = party
        bar_colors = ['tab:orange', 'tab:green']

        ax.bar(party, counts, label=bar_labels, color=bar_colors)

        ax.set_ylabel('Votes each Party Got')
        ax.set_title('Election results of 2024')
        ax.legend(title='Election results')

        plt.show()

candidateList = [
    {"name": "prabhu", "party": "BJP", "total": 0},
    {"name": "rohan", "party": "Congress", "total": 0}
]

v = Voting(candidateList)

votersInLine = [
    {"name": "abcd", "age": 20, "votingFor": "BJP"},
    {"name": "yz", "age": 20, "votingFor": "Congress"},
    {"name": "abcd", "age": 20, "votingFor": "BJP"},
    {"name": "yz", "age": 20, "votingFor": "Congress"},
    {"name": "yz", "age": 20, "votingFor": "BJP"},
    {"name": "yz", "age": 20, "votingFor": "Congress"},
    {"name": "abcd", "age": 20, "votingFor": "BJP"},
    {"name": "yz", "age": 20, "votingFor": "Congress"},
    {"name": "yz", "age": 20, "votingFor": "BJP"},
     {"name": "yz", "age": 20, "votingFor": "Congress"},
      {"name": "yz", "age": 20, "votingFor": "Congress"},
       {"name": "yz", "age": 20, "votingFor": "Congress"},
        {"name": "yz", "age": 20, "votingFor": "Congress"},
     {"name": "yz", "age": 20, "votingFor": "BJP"},
      {"name": "yz", "age": 20, "votingFor": "BJP"},
       {"name": "yz", "age": 20, "votingFor": "BJP"},
        {"name": "yz", "age": 20, "votingFor": "BJP"},
]

for item in votersInLine:
    v.startVoting(item)

v.showVictory()
v.showIngrapgh()
