1. The [Box Model] is essentially the idea that everything in CSS is a box.
		-->Content Box
		-->Padding
		-->Border
		-->Margin
2. [Width] & [Height] that sets the width and height of the inner content area. 
3. [Border] is the property that is around an element. It can be short-handed so you put all the information in one line instead of multiple lines. The order is: width, style, color. 
		-->Border-Width
		-->Border-Color
		-->Border-Style
4. [Padding] is the space between the content and the content box and the border of the box. You can set top/bottom & left/right simultaneously by setting padding: 10px 20px; top - right - bottom - left
	-->Individual properties: padding-left, padding-right, padding-bottom, padding-top
	-->Shorthand property: set all four sides at once.
5. [Margin] is the space outside of an element's border between that element and another element. Margin is similar to padding with the same settings. 
	-->Individual properties: margin-left, margin-right, margin-bottom, margin-top
	-->Shorthand properties: set all four sides simultaneously.
6. [Display Property]
	-->Inline: Width & Height are ignored. Margin & padding push elements away horizontally but not vertically.
	-->Block: Block elements break the flow of a document. Width, Height, Margin, & Padding are respected. 
	-->Inline-Block: Behaves like an inline element execpt Width, Height, Margin, & Padding are respected. 
6. CSS Units:
	-->EM: Relative units. 1em = font-size of the parent. 2em = twice the font-size of the parent. Allows you to scale easily. However, they stack and can grow and shrink significantly
	-->REM: Relative to the root html element's font-size. Often easier to work with. Example: if root font-size= 20px, 1 rem is always 20px, 2 rem is always 40 px, etc. 
	-->VH
	-->VW
	-->%: Percentages are always relative to some other value. (Example: width: 50% - half the width of the parent)