# Tutorial on Advanced Positioning Techniques like relative, absolute, fixed

link to the article: https://internetingishard.com/html-and-css/advanced-positioning/

### Take-aways

1. **The position: relative;** line makes it a positioned element, and the top and left properties let you define how far it’s offset from its static position. This is sort of like setting an (x, y) coordinate for the element.

Relative positioning works similarly to margins, with one very important difference: neither the surrounding elements or parent element are affected by the top and left values.

Everything else renders as if .item-relative was in its original position.

Think of the offsets as being applied after the browser finishes laying out the page.

2. **“Absolute positioning”** is just like relative positioning, but the offset is relative to the entire browser window

The other interesting effect of absolute is that it completely removes an element from the normal flow of the page.

3. **(Relatively) Absolute Positioning**

Absolute positioning becomes much more practical when it’s relative to some other element that is in the static flow of the page. Fortunately, there’s a way to change the coordinate system of an absolutely positioned element.

 **Coordinates for absolute elements are always relative to the closest container that is a positioned element.**

 Coordinates for absolute elements are always relative to the closest container that is a positioned element. It only falls back to being relative to the browser when none of its ancestors are positioned. So, if we change .item-absolute’s parent element to be relatively positioned, it should appear in the top-left corner of that element instead of the browser window.

4. **(Fixed Positioning)**
   “Fixed positioning” has a lot in common with absolute positioning: it’s very manual, the element is removed from the normal flow of the page, and the coordinate system is relative to the entire browser window. The key difference is that fixed elements don’t scroll with the rest of the page.

   

   This will place the red image in the bottom-right corner of the screen. Try scrolling the page, and you’ll discover that it doesn’t move with the rest of the elements on the page, while the absolutely positioned purple image does.

   This lets you create navigation bars that always stay on the screen, as well as those annoying pop-up banners that never go away.



## Summary

static is the default positioning of every element

relative is positioning relative to the static position of the element itself

absolute - useless. But it is absolute to ancestor's relative, if no such thing, then web browser window. Use only if there is ancestor relative.

fixed - like absolute but does not support scrolling.




