
* walking through code with debugger for understanding code.

So basically anytime I do
something clever, I make sure I have a test in there to break really loudly

It’s one thing to go
learn a language for fun, but until you write some big, complex system in it,
you don’t really learn it.

Seibel: How do you design software?
Fitzpatrick: I start with interfaces between things. What are the common
methods, or the common RPCs, or the common queries. If it’s storage, I try
to think, what are the common queries? What indexes do we need? How
are the data going to be laid out on disk? Then I write dummy mocks for
different parts and flesh it out over time.
Seibel: Do you write mocks in the test-first sense so you can test it as you
go?
Fitzpatrick: More and more. I always designed software this way, even
before testing. I would just design interfaces and storage first, and then
work up to an actual implementation later.
Seibel: What form would the design take? Pseudocode? Actual code?
Whiteboard scribbles?
Fitzpatrick: Generally I would bring up an editor and just write notes with
pseudocode for the schema. After it got good, I would make up a real
schema and then I would copy-paste it in just to make sure that “create
table” works. Once I got that all going, I’d actually go implement it. I always
start with a spec.txt first.

Seibel: Do you have any advice for self-taught programmers?
Fitzpatrick: Always try to do something a little harder, that’s outside your
reach. Read code. I heard this a lot, but it didn’t really sink in until later.

Seibel: What are your debugging tools? Debuggers? Printlns? Something
else?
Fitzpatrick: Println if I’m in an environment where I can do that.
Debugger, if I’m in an environment that has good debuggers. GDB is really
well maintained at Google and is kind of irreplaceable when you need it. I
try not to need it too often. I’m not that great at it, but I can look around
and kind of figure things out generally. If I have to go in there, I generally can
find my way out. I love strace. Strace, I don’t think I could live without. If I
don’t know what some program is doing, or what my program is doing, I
run it under strace and see exactly what’s happening. If I could only have
one tool, it would probably be that. All the Valgrind tools, Callgrind and all
that, those are good.

But a lot of times lately, if there’s something weird going on, I’m like, “OK,
that function is too big; let’s break that up into smaller parts and unit-test
each one of them separately to figure out where my assumptions are wrong,
rather than just sticking in random printlns.”
Then maybe in the process of refactoring, I have to think about the code
more, and then it becomes obvious. I could, at that point, go back to the
big, ugly state where it was one big function and fix it but I’m already
halfway there; I might as well continue making it simpler for the next
maintainer.

Seibel: How do you use invariants in your code? Some people throw in ad
hoc asserts and some people put in invariants at every step so they can
prove formal properties of their programs, and there’s a big range in the
middle.

Fitzpatrick: I don’t go all the way to formal. My basic rules is, if it could
possibly come from the end user, it’s not a run-time crash. But if it is my
code to my code, I crash it as hard as possible—fail as early as possible.
I try to think mostly in terms of preconditions, and checking things in the
constructor and the beginning of a function. Debug checks, if possible, so it
compiles away. There are probably a lot of schools of thought and I’m
probably not educated about what the proper way to do it is. There are
languages where all this stuff is actually a formal part of the language. Pretty
much all the languages I write in, it’s up to you.

Seibel: What do you think is the most important skill for a programmer to
have?
Fitzpatrick: Thinking like a scientist; changing one thing at a time. Patience
and trying to understand the root cause of things. Especially when you’re
debugging something or designing something that’s not quite working. I’ve
seen young programmers say, “Oh, shit, it doesn’t work,” and then rewrite
it all. Stop. Try to figure out what’s going on. Learn how to write things
incrementally so that at each stage you could verify it.

===============================================================================