☯️ Glyphic Language — BNF Grammar Specification (v1.0)
Formal Grammar for the Glyphic OS Interpreter
This grammar defines the canonical structure of a valid glyph sequence.
It is strict, deterministic, and reversible.


1. Top‑Level Grammar
Code
<glyph-sequence> ::= <actor-block> <action-block> <object-block> <modifier-block> <context-block>
A valid sequence must follow this order.
All blocks are optional except that at least one of:
    <actor-block>
    <action-block>
    <object-block>
must be present.


2. Actor Block
Code
<actor-block> ::= <actor> | ε
<actor>       ::= <glyph-actor>
Constraints:
    Only one actor allowed.
    If present, it must appear first.


3. Action Block
Code
<action-block> ::= <action> | ε
<action>       ::= <glyph-action>
Constraints:
    Only one action allowed.
    Must appear after actor, if actor exists.


4. Object Block
Code
<object-block> ::= <object> | ε
<object>       ::= <glyph-object>
Constraints:
    Only one primary object allowed.
    Must appear after action, if action exists.


5. Modifier Block
Code
<modifier-block> ::= <modifier-list> | ε
<modifier-list>  ::= <modifier> <modifier-list> | <modifier>
<modifier>       ::= <glyph-modifier>
Constraints:
    Zero or more modifiers allowed.
    Must appear after object, if object exists.
    Modifiers cannot appear after context.


6. Context Block
Code
<context-block> ::= <context-place-block>
                    <context-time-block>
                    <context-emotion-block>
                    <context-sensory-block>
                    <context-social-block>
Each context subtype is optional, but must appear in this order if present.


7. Context Subtypes
Place Context
Code
<context-place-block> ::= <context-place-list> | ε
<context-place-list>  ::= <context-place> <context-place-list> | <context-place>
<context-place>       ::= <glyph-context-place>
Time Context
Code
<context-time-block> ::= <context-time-list> | ε
<context-time-list>  ::= <context-time> <context-time-list> | <context-time>
<context-time>       ::= <glyph-context-time>
Emotional Context
Code
<context-emotion-block> ::= <context-emotion-list> | ε
<context-emotion-list>  ::= <context-emotion> <context-emotion-list> | <context-emotion>
<context-emotion>       ::= <glyph-context-emotion>
Sensory Context
Code
<context-sensory-block> ::= <context-sensory-list> | ε
<context-sensory-list>  ::= <context-sensory> <context-sensory-list> | <context-sensory>
<context-sensory>       ::= <glyph-context-sensory>
Social Context
Code
<context-social-block> ::= <context-social-list> | ε
<context-social-list>  ::= <context-social> <context-social-list> | <context-social>
<context-social>       ::= <glyph-context-social>


8. Glyph Terminals
These terminals correspond directly to dictionary roles.
Code
<glyph-actor>            ::= any glyph with role "actor"
<glyph-action>           ::= any glyph with role "action"
<glyph-object>           ::= any glyph with role "object"
<glyph-modifier>         ::= any glyph with role "modifier"
<glyph-context-place>    ::= any glyph in category "context_place.*"
<glyph-context-time>     ::= any glyph in category "context_time.*"
<glyph-context-emotion>  ::= any glyph in category "context_emotion.*"
<glyph-context-sensory>  ::= any glyph in category "context_sensory.*"
<glyph-context-social>   ::= any glyph in category "context_social.*"
These terminals are not literal characters — they are semantic classes defined by the dictionary.


9. Role Precedence (Disambiguation Rule)
If a glyph has multiple roles (rare but allowed), precedence is:
Code
actor > action > object > modifier > context
This ensures deterministic parsing.


10. Validity Constraints (Non‑BNF but Required)
These constraints are enforced by the interpreter:

10.1 Required Core Role
At least one of:
    actor
    action
    object
must be present.

10.2 Context Must Be Last
No context glyph may appear before:
    actor
    action
    object
    modifier

10.3 Single Actor / Action / Object
Only one of each is allowed.

10.4 Context Ordering
Context subtypes must appear in this order:
Code
place → time → emotion → sensory → social

10.5 Reversibility
All valid sequences must satisfy:
Code
encode(decode(sequence)) == sequence
This is guaranteed by the grammar.


11. Example Valid Sequences
Actor + Action + Object
Code
<actor> <action> <object>
Object + Modifier + Context
Code
<object> <modifier> <context-place> <context-time>
Action + Context
Code
<action> <context-emotion> <context-social>
Full Scene
Code
<actor> <action> <object> <modifier> <context-place> <context-time> <context-emotion> <context-sensory> <context-social>


12. Example Invalid Sequences
❌ Context before object
Code
<context-place> <object>
❌ Multiple actions
Code
<action> <action>
❌ Social context before sensory context
Code
<context-social> <context-sensory>
❌ No core role
Code
<modifier> <context-place>
