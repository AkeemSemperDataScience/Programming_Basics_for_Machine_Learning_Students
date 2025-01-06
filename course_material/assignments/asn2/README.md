# Programming Basics for ML - Assignment #2

Some hints and notes:
<ul>
<li> Tackle things in chunks: </li>
    <ul>
    <li> Can you read in the data, and isolate what you care about? </li>
    <li> Can you make a child list that does nothing special, but inherits from the parent list and works? </li>
    <li> Can you use that to make the core functionality (prining until the threshold is met) work, one addition/chage at a time? </li>
    <li> Can you make the child list flexible? I.e. different lengths, types, etc. </li>
    <li> Can you then add other assorted functionality (error checks, useful functions, etc...) child list? </li>
    <li> Can you then add the inputs and outputs to make testable data? </li>
    </ul>
<li> You can almost certainly make a constantly working versions of this, then add steps one by one to make the output move towards what you want. </li>
<li> Focus on inputs and outputs - you have both. What steps need to go in between? Making one step work at a time will eventually get you there. </li>
<li> If you have one "step" at a time, ideally in its own function, you can test it even before you have the whole thing working. </li>
<li> The input file can have an arbitrary number of columns of values - you should use however many are filled with data, and ignore the rest. </li>
</ul>
