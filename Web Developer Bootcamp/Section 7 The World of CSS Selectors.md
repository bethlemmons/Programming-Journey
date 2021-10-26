1. CSS [[Selectors]]
2. The [[universal selector]] "* " selects all of something. Example: * { background-color: cyan; }. Not commonly used.
3. The [[element selector]] selects everything of a given type. Example: button { font-size: 30px}.
4. The [[selector list]] allows you to use a comma to combine multiple selectors in a list. Example: h1, h2 {color: magenta;}
5. The [[id selector]] can be used for any element to single out a specific "hook" for CSS to use. Example: <button id="signup">Sign Up</button>. To call this id/"hook" for CSS, you need to use "#". Example: #signup{background-color: blue;}
6. The [[class selector]] is similar to id but it can be applied to multiple elements. Can grab multiple elements simultaneously. Need to use "." for class.
7. The "#" symbol is used for id. It is important to keep the symbol for class and the symbol for id straight. 
8. The [[descendent selector]] allows you to select something that is nested within a li. Example: li a {
                         color: teal;
						 }
9. [[Adjacent Selector]] (combinator) allows you to select paragraphs that immediately proceed the called element. 
    Example: h1 + p {
	                       color: red;
						   }
10. [[Direct Child]] (combinator) allows you to select the direct descendent/child of an element 
      Example:  div > li {
	                        color: white; 
							}
11. [[Attribute Selector]] allows you to select a specific type of attribute.  
      Example: input[type="text"] {
	                      width: 300px;
						  color: yellow;
						  } 
12. Pseudo Classes are keywords added to a selector that specifies a special state of the selected elements. 
	                  --> :active
					  -->:checked
					  -->:first
					  -->:first-child
					  -->:hover
					  -->:not()
					  -->:nth-child()
					  -->:nth-of-type()
13. Pseudo Elements are keywords added to a selector that lets you style a particular part of a selected element:
	-->::after
	-->::before
	-->::first-letter
	-->::first-line
	-->::selection
14. The CSS Cascade: The order that styles are declared in does matter. The last called style is the one that will win. 
15. Specificity is how the browser decides which rules to apply when multiple rules could apply to the same element. It is a measure of how specific a given selector is. The more specific selector "wins". ID > CLASS > ELEMENT
16. CSS Dev tools in Chrome. Inspect. Bottom half allows you to dive deeper into the code and even shows you elements that aren't being utilized and why. 
17. Inline styles --> More specific that ID selectors. But people don't use them often. Generally avoid them because they are confusing.
18. !Important rules-->generally not recommended. When you assign some style as !important, it signals to the browser that it is the most important/specific thing. 
19. CSS Inheritance --> Some CSS properties are inherited by children if they aren't explicitly set to something else. The "child" properities will always inherit the properities of whatever parent element is closest. 