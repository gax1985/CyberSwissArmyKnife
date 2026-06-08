
# Dangerous Regex Statements


[regex101: build, test, and debug regex](https://regex101.com/)

![[Pasted image 20251014091611.png]]
>Regex101.com : `Regex Playground`


Regex statements have the potential of bringing down systems due to the complexity of the statement. 


>[!example]
>
>Please examine the following statement : 
>
>`1/^(a+)+$`

  
^(a+)+$

/

gm

^ asserts position at start of a line

1st Capturing Group

(a+)+

+ matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy)

A repeated capturing group will only capture the last iteration. Put a capturing group around the repeated group to capture all iterations or use a non-capturing group instead if you're not interested in the data

a

matches the character a with index 9710 (6116 or 1418) literally (case sensitive)

+ matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy)

$ asserts position at the end of a line

Global pattern flags

g modifier: **g**lobal. All matches (don't return after first match)

m modifier: **m**ulti line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
