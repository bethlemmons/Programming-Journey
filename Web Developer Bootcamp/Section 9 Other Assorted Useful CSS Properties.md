1. Opacity-->Is a property that we set on an element that governs it's transparency and any of its descendants. 0-1. It controls everything in the element. 
2. Alpha Channel--> Value 0-1. Transparent-Solid. This allows elements to be transparent. Example: rgba(255, 255, 255, 0.7)
3. Position --> Property that sets how an element is positioned in a document. The top, right, bottom, and left properties determine the final location of positioned elements. 
		-->static
		-->relative: changes its position relative to its original position. 
		-->fixed: removes element from normal document flow and no space is created for the element in the page layout. It is positioned relative to the initial containing block established by the viewport. 
		-->absolute: removes the element from the normal document flow and no space is created for the element in the page layout. It is positioned relative to its closest positioned ancestor.
		-->sticky: allows an element to stay in-line until scrolling starts and then it will keep it at the top of the block. 
	4. Transitions -->allow us to animate the transition of one property to another property.
			-->Property name: You can use a specific property name to identify the aspect you want to adjust.
			-->Duration: The length of time designated for a transition.
			-->Timing Function:
			-->Delay: 
	5. Transform --> Allows you to move elements in particular ways. Can do this all in one line. Example: transform: rotate(20deg) scale(1.3);
			-->Rotate: Angles, gradient, radians, turns. 
			-->Scale: Changes the size of the element.
			-->Translate: Allows you to move the element up/down/sideways.
			-->Skew: Allows you to move an element at an angle.
	6. Box-Shadow --> this property adds shadow effects around an element's frame. You can set multiple effects separated by commas. 
	7. Background --> order doesn't generally matter except background size may only be included immediately after position. 
			-->background-image: allows you to set a background image and gradient. Use Unsplash as a resource for images. 
			-->background-size: sets the size of the element's background image. The image can be left to its natural size, stretched, or contstrained to fit the available space. 
					>contain --> scales the image as large as possible without cropping or stretching the image.
					>cover --> scales the image as large as possible without stretching but will crop it so no empty space remains.
					>auto --> scales the image in the corresponding direction so that that its intrinsic proportions are maintained.
					><length>
					><percentage>
	8. Google Fonts --> 