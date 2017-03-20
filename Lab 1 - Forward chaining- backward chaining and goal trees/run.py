from production import IF, AND, OR, NOT, THEN, DELETE, forward_chain 
 
theft_rule = IF('you have (?x)',
                 THEN( 'i have (?x)' ),
                 DELETE( 'you have (?x)' ))
 
data = ( 'you have apple','you have orange','you have pear' ) 
 
print(forward_chain([theft_rule], data, verbose=True))
