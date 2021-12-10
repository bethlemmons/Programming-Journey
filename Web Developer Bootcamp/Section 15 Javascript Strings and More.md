1. [Strings] are another primitive type in JavaScript. They represent text and must be wrapped in quotes. 
2. Need to remain consistent between single quotes and double quotes
3. Strings are indexed meaning each character has a corresponding index (a positional number).
4. [Concatenation] is the combination of two strings.
5. [String Methods] are built-in actions we can perform with individual strings. They help with searching within a string, replacing part of a string, or changing the casing of a string.
	-->thing.length: the dot something is accessing a variable's properties.
	-->thing.method(): is accessing a method.
	--> [Trim] : method used for trimming white space in a string. 
	-->You can combine multiple methods simultaneously. They can be chained together. 
6. Many [methods] accept [arguments] to be passed into the method.
	-->thing.method(arg)
	-->indexOf is an argument that tells you where ther first occurance of a specific example it. Usually used to see if string contains a specific something such as $, %, etc. 
	-->str.slice()
	-->str.replace(replace, replacement)
6. [Template Literals] are sthrings that allow embedded expressions, which are evaluated and then turned into a resulting string. 
	--> MUST use back-tick characters, not single brackets. Found above the tab key.
	--> ex: `I counted ${3 + 4} sheep`;
	--> The expression within the dollar sign and back-ticks will be evaluated. It allows you to directly imbed variables inside a string. 
7. [Null & Undefined]
	-->Null: Intentional absence of any value. Must be assigned.
	-->Undefined: Variables that do not have an assigned value are undefined.
8. [Math Object] Containers properties and methods for mathematical constants and functions. 