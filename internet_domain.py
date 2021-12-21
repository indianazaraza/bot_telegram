import pandas

class InternetDomains():
    def __init__(self, data_domains:list):    
        # convert list to dataframe
        self.dataframe = pandas.DataFrame(data_domains)
        # filter columns 
        self.dataframe = pandas.concat([self.dataframe["domain"], 
                                        self.dataframe["isDead"]], axis=1)
        self.dataframe.rename(columns={"domain":"Domains", "isDead":"Status"}, inplace=1)
        # change values at status column 
        self.dataframe["Status"] = self.dataframe["Status"].map({
            "False":"Active", "True":"Inactive"}, na_action=None)
    
    def status_amount(self, status):
        # get the number of domains according to the states
        return self.dataframe.groupby(["Status"]).count().loc[status, "Domains"]

    def active_domains(self):
        # get the number of active domains 
        return self.status_amount("Active")

    def inactive_domains(self):
        # get the number of active domains 
        return 0 if (self.active_domains() <= 50) else self.status_amount("Inactive")

    def list_domains(self):
        # get list with domain names
        return self.dataframe["Domains"].head(10).to_string(index=False)