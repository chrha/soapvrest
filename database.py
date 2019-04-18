class Database(object):

    """Class containing a database implementation."""

    def __init__(self, db_file):
        self.db_file = db_file
        self.msg=open(self.db_file,'r')
        self.parsed_file=[]
        entire_line=""
        for line in self.msg:
            entire_line+=line
            if(line[0]=="%" and line[1]=="\n"):
                self.parsed_file.append(entire_line[0:-3])
                entire_line=""
        self.msg.close()

    def read(self,uid):
        """Read a random location in the database."""
        if not self.parsed_file:
            return "" #raise Exception("Empty database")
        else:
            return self.parsed_file[uid]

    def read_all(self):
        """Read a random location in the database."""
        if not self.parsed_file:
            return "" #raise Exception("Empty database")
        else:
            return self.parsed_file

    def write(self, fortune):
        """Write a new fortune to the database."""
        self.parsed_file.append(fortune)
        new_line=fortune + "\n" + "%" + "\n"
        message=open(self.db_file,'a')
        message.write(new_line)
        message.close()
