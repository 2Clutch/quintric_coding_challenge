# quintric_coding_challenge

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/75ee19ad1d7444c3872c400835ec5b2c)](https://app.codacy.com/app/2Clutch/quintric_coding_challenge?utm_source=github.com&utm_medium=referral&utm_content=2Clutch/quintric_coding_challenge&utm_campaign=badger)
[![StackShare](https://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/2Clutch/knowledge-purse)

This project is a simple command line application which can be used to view the balances of any given BitShare users.

# Setup

First, you will want to clone the repository using the following command:
```commandline
git clone https://github.com/2Clutch/quintric_coding_challenge
```

To interact with the blockchain, I used [pybitshares](http://docs.pybitshares.com/en/latest/index.html). According to their documentation, there are 2 ways to install the library. I went with `pip3`, running:
```commandline
sudo apt-get install libffi-dev libssl-dev python-dev python3-dev python3-pip
pip3 install bitshares
```

Just for clarification, each line above represents a command to be ran independently. Once that's taken care of, navigate to the project's directory and run:
```commandline
python3 bitshares.py -u [insert_user_name_here]
```

<br>

![alt_text](sample_output.png)
