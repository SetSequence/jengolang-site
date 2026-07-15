# HISTORY — Grammar skill-tree build log (archived from TREE.md)

Append-only. Not needed for forward work — the live cursor is `PASS.md`,
the design is `TREE.md`. Kept for provenance / debugging a past decision.

---

## Pass-2 dated build log

**STRUCTURAL — Arc 1 adjectives + follow-ups DONE (2026-07-15, second session):** filled
the **adjective hole** flagged in the Arc-1 reorder. Introduced a new `adjective` family
(registered in `build_slice.py` FAMILY_ORDER, `lib/grammar.ts` FAMILY_ORDER+FAMILY_LABEL,
`qa_grammar_nodes.py` FAMILY) and authored two net-new indexed Foundations nodes —
`i-adjective` (高い/高くない/高かった/高く + いい irregular; self-contained) and `na-adjective`
(leads with polite です-forms since plain だ/じゃない land in the next unit; cross-links
kute/de-3/ni-naru). Placed as a **new Arc-1 unit 4 "Describe things: い and な adjectives"**
(after existence U3, before plain form) via a **global spine renumber**: old units 4–55 →
5–56; edited `ARC_RANGES` (Arc 1 now 1–11, every later arc +1), `UNIT_LABELS` (1–21),
`FOUNDATION_STAGES` (11 stages), shifted all 1,391 `spine_units.csv` rows with unit_index≥4,
and added 2 catalog rows. Catalog **1,460 → 1,462**; indexed **1197 → 1199**; slice validates
**56 units / 9 arcs**, Foundations **70 → 72 nodes**. Rendering is fully data-driven from
`grammar_slice.json`, so no `.astro`/`.ts` unit literals needed touching. **Also:** demoted
Japanese-linguistics-jargon `title`s to lead with plain English on verb-classes / ta-form /
volitional-form (on-path) + te-form / masu-stem / nai-form / ba-conditional (off-path),
keeping `canonical` intact; and rewrote 8 forward-reference example lines (て-form/ている/
てください/てもいい/ましょう used before U5–U7) across yo/e/o/to-2/ni-2/made/ta-form to use
only ≤-unit grammar. build_slice PASS · lint clean · npm build clean · qa_grammar_nodes PASS.

**BUILD common batch 1 DONE (2026-06-14):** first `--freq common` batch (182 → **192
indexed**). Cluster = question words + indefinites + degree/quantity adverbs (N5), chosen
for dense cross-linking. First batch to use the **cluster-prep subagent** (Explore agent →
brief: per-stub frontmatter, valid enriched contrast targets, homograph traps, sub-cluster
map — externalized ~10 grep round-trips). **10 indexed:** interrogatives (dou how/how-about,
doushite why, douyatte how-by-means, donna what-kind — mutually contrasted + donna↔konna),
indefinites (dareka-dokoka, nani-ka-nani-mo — the か=some / も+neg=none system, cross-linked
+ to mo), degree (amari not-very, anmari colloquial, takusan a-lot, sugiru too-much —
triangulated with the already-indexed zenzen/totemo). **1 kept noindex by design:** ka-2 (か
'or') — redundant with the enriched `ka` (question/or/embedded), thin redirect-hub (the
cluster-prep brief flagged the duplicate-content risk; same call as the essentials folds).
Confidence upgrades dou med→high, takusan med→high (meaning never shaky). All 1,458
pages build PASS, lint clean (scripts/lint_batch.py), ruby verified.
**amari resolved (2026-06-14, user DBJG check):** DBJG treats あまり and あまりに as **two
separate nodes** — confirmed `amari-2` (あまり(に)〜 'so/excessively') and `amari-ni-mo`
(あまりにも) already exist as stubs. So `amari` is cleanly single-sense 'not very' (spoken
あんまり): dropped the free-floating あまりに note, added a `contrasts` link to amari-2, bumped
med→high. **Next: common batch 2.**

**BUILD common batch 2 DONE (2026-06-15):** N4 degree + progression adverbs (192 → **204
indexed**, 12 nodes). Cluster chosen to triangulate against the already-indexed degree
siblings (totemo, amari, anmari, takusan, sugiru, zenzen, motto, mou, sugu) for a dense
contrast web. **12 indexed:** degree/intensity — hijouni (非常に formal 'extremely'),
hontou-ni (本当に 'really', sincerity nuance), taihen (大変 **multi-sense:** ①polite 'very'
intensifier / ②な-adj 'tough/serious'), sonna-ni (そんなに 'that much', context-referenced),
zenzen-nai (全然〜ない total negation, +note on colloquial 全然+positive), nakanaka-nai
(なかなか〜ない 'won't easily', impatience nuance); progression/time — dandan↔dondon
(gradual vs fast, mutually contrasted), zutto (**multi-sense:** ①duration / ②'by far' —
contrast to motto pinned sense ②), ichido (一度 'once'), mo-sugu (もうすぐ 'soon', contra
sugu/mou), sakki (さっき 'a while ago', casual-only, contra 先ほど). **Gotcha logged:**
`usageSetting` and `nuance` are scalar **strings** in the schema, not arrays — first build
failed on dandan with "Expected string, received object"; fixed across 7 files. All 1,458
pages build PASS, lint clean, ruby verified. **Next: common batch 3** (adverbial family
still rich — N4 certainty/frequency kitto/kanarazu/itsu-de-mo, N3 degree kanari/kekkou).

**BUILD common batch 3 DONE (2026-06-15):** negative-polarity / total-negation adverbs
(204 → **215 indexed**, 11 nodes + 1 noindex redirect). The densest contrast web yet — a
notoriously confusable set built on a shared 'XXX〜ない' frame, all cross-linked to the
batch-2 zenzen-nai/nakanaka-nai and the enriched amari. **The GEO spine = a degree scale of
negation:** あまり〜ない (not very) → ほとんど〜ない (hardly) → 全然/全く〜ない (not at all,
zero); plus めったに〜ない (seldom — frequency) vs 決して〜ない (never — resolve). **11
indexed:** hotondo (ほとんど positive 'almost/most') + hotondo-nai (ほとんど〜ない 'hardly');
mattaku (全く positive 'completely', +exasperation note) + mattaku-nai (全く〜ない, formal/
emphatic twin of 全然〜ない); chittomo (casual+peevish); sappari (さっぱり〜ない 'no clue/no
progress', +note on unrelated さっぱりする 'refreshed'); metta-ni (frequency); kesshite
(resolve/principle, warnings); betsu-ni-nai (dismissive 'not particularly', +別に。curt
reply); sukoshi-mo (少しも〜ない 'not in the slightest', formal twin of ちっとも); totemo-nai
(とても〜ない = 'cannot possibly' — **restriction node**: the classic 'not very' misread,
pairs with a potential-negative). **1 noindex redirect:** sukoshi-mo-nai → sukoshi-mo (少しも
has no positive use, so 少しも and 少しも〜ない are one pattern; indexed the high-conf headword
sukoshi-mo, kept sukoshi-mo-nai (conf med) as a navigable duplicate-surface redirect — the
ka-2/de-iru pattern; still counts as a stub in list_stubs by design). **Polarity-split rule:**
全く and ほとんど genuinely split positive vs negative → both halves indexed as distinct nodes;
少しも does not. All 1,458 pages build PASS, lint clean, ruby verified. **Next: common batch
4** (certainty/likelihood adverbs, or '+' intensifiers kanari/kekkou/daitai).

**BUILD common batch 4 DONE (2026-06-15, larger batch):** two internally-dense adverbial
sub-clusters (215 → **230 indexed**, 15 nodes). First batch run at the larger size the user
asked for. **(a) Epistemic certainty/probability adverbs (10)** — the speaker-confidence
scale, the certainty analog of batch-3's negation spine, all pairing with the modality family
(でしょう/だろう/かもしれない/ようだ): 必ず kanarazu (objective 100% guarantee/'be sure to') ·
きっと kitto (confident subjective guess) · おそらく osoraku (formal hedged 'probably', N2) ·
もしかしたら moshika-shitara (coin-flip 'maybe', +variants もしかすると/もしかして) · まさか masaka
(incredulous 'surely not') · 確かに tashika-ni (acknowledging 'indeed', concession-setup;
+note 確か≠確かに) · 間違いなく machigai-naku ('without doubt', guarantee) · 必ずしも〜ない
kanarazushimo (partial negation 'not necessarily' — links 必ず + batch-3 zenzen-nai) · 明らかに
akiraka-ni (evidence-certain 'clearly') · どうやら dou-yara (evidential 'apparently', pairs
ようだ/らしい). Cross-contrasted along the confidence axis + zettai-ni. **(b) Positive '+'
intensifiers (5)** — degree ladder 少し<結構<かなり<とても/非常に: かなり kanari · 結構 kekkou
(**multi-sense:** ①degree 'quite' / ②結構です 'fine/no thanks' — the famous accept-vs-decline
ambiguity, flagged in a note) · だいたい daitai ('roughly/mostly', +sentence-head 'to begin
with' note, contra ほとんど) · なかなか nakanaka (positive 'impressively', admiring-surprise
nuance; closes the loop with batch-3 nakanaka-nai) · 最も mottomo (formal superlative, contra
一番; +homograph note 最も≠尤も/もっとも conj). All 1,458 pages build PASS, lint clean (15),
ruby verified. **Next: common batch 5** (conclusion/result 'finally' adverbs, or pivot off
the adverbial family to modality/connectives for variety).

**BUILD common batch 5 DONE (2026-06-15, big-batch sweep):** 30 adverbial stubs in one pass
(230 → **258 indexed**, 28 indexed + 2 redirects) — user pushed batch size up twice; ~30 held
fine (lint + build green, quality high). Four internally-dense sub-clusters that largely
**drain the adverbial family**: **(A) culmination 'finally' (7)** — やっと yatto (relief) /
ついに tsui-ni (climax) / とうとう toutou (inevitable, often negative) / 漸く youyaku (formal) /
いよいよ iyoiyo (imminent climax) / 結局 kekkyoku (net conclusion) / やがて yagate (literary
'before long', contra batch-2 mo-sugu) — the classic やっと≠ついに≠とうとう≠結局 confusion,
mutually contrasted. **(B) stance: as-expected / anyway / first-place (6 + 2 redirect)** —
やはり yahari (indexed, with やっぱり as a register **variant**; yappari + yahari-yappari →
noindex redirects, the 3-node-for-1-word dedup) / さすが sasuga (admiring) vs さすがに sasuga-ni
(concessive limit) / とにかく tonikaku / どうせ douse (resigned) / そもそも somosomo (contra
batch-4 daitai's reproachful 'to begin with'). **(C) timing / suddenness / already (8)** —
いきなり ikinari (abrupt onset) / たちまち tachimachi (fast spread) / 一気に ikki-ni (one burst,
contra batch-2 dondon) / いつの間にか itsu-no-ma-ni-ka / とっくに tokku-ni / 既に sude-ni (formal
'already', contra essential もう) / 未だに imada-ni (contra essential まだ) / 直ちに tadachi-ni
(formal 'immediately', contra essential すぐ). **(D) manner / effort / provisional (7)** —
わざわざ wazawaza vs せっかく sekkaku (trouble-taking vs precious-chance) / なるべく naru-beku /
思うように omou-you-ni / とりあえず toriaezu vs 一応 ichiou (first-step vs just-in-case) / せめて
semete (wished minimum, contra 少なくとも). **Two slips caught:** a stray English word in a
tadachi-ni jp example (→ 操業), and a self-referential contrast slug on naru-beku (→ moved to
note). All 1,458 pages build PASS, lint clean (30), ruby + ASCII-scan verified. **Next:
common batch 6 — PIVOT off adverbials** to modality (〜はず/〜わけ/〜べき) or connectives.

**BUILD common batch 6 DONE (2026-06-15, the modality pivot):** the appearance / evidentiality
/ hearsay web — 9 stubs, **8 indexed + 1 redirect-hub** (258 → **266 indexed**). First
non-adverbial cluster, chosen for contrast density and it delivered: みたい mitai (casual ようだ,
2 senses: conjecture + resemblance, with the no-の/な attachment restriction vs ようだ) · みたいだ
mitaida (**redirect-hub → mitai**, kept noindex to avoid duplicate-content tax — same treatment
as foldInto) · みたいに・みたいな mitai-ni (adverbial/adnominal, ↔ ように・みたい) · そうだ-様態
souda-2 (appearance + imminent senses; **stem** attachment) ↔ そうだ-伝聞 souda (hearsay, family
quotation; **plain-form** attachment) — the classic 降りそう≠降るそう minimal pair, mutually
contrasted · そうに・そうな sou-ni (adverbial/adnominal of 様態そう; fixed its seeded prereq
souda→souda-2) · らしい rashii (2 senses: inference/hearsay + 'befitting', with the mandatory
らしい≠っぽい contrast) · 〜に見える ni-mieru (strictly-visual 'looks ~') · 〜ような yona (adnominal
of ようだ; **rewrote the bundled 〜ような/〜よな title** down to 〜ような, demoted 〜よな to a variant
note; confidence stays med). Dense anchors reused: ようだ, ように, っぽい, かもしれない. **One trap
caught:** `variants[]` items are `form:` (+ optional `note:`), NOT `text:` — used `text:` and
the build rejected it; fixed across the batch, folded into PASS §4. All 1,458 build PASS, lint
clean (9).

**BUILD common batches 7–9 DONE (2026-06-15, multi-cluster sweep):** per user directive to
stop checkpointing at every cluster and roll several per turn, three modality clusters in one
turn — 33 nodes, all indexed (266 → **299 indexed**), one consolidated build PASS, lint clean
(33). **Batch 7 — necessity/obligation (9):** the colloquial-ellipsis 'must' forms ないと
naito / なくては nakute-wa (trailed-off いけない) and their casual contractions なくちゃ naku-cha
(← なくては) / ちゃいけない cha-ikenai (← てはいけない, with the ては→ちゃ・では→じゃ voicing
rule), the 必要 trio 〜が必要 ga-hitsuyou (noun) vs 〜必要がある hitsuyou-ga-aru (action) vs 〜必
要はない hitsuyo-wa-nai, plus 〜なくて済む nakute-sumu (spared having to) and 〜ざるを得ない
zaru-o-enai (formal 'forced to'; する→せざる irregular). Anchored to the already-enriched core
(なければならない, てはいけない, なくてもいい). **Batch 8 — はず/わけ/べき expectation-logic
(13):** はずだ hazu-da (expectation) / はずがない hazu-ga-nai, the わけ family わけだ wake-da
('no wonder') / わけではない wake-de-wa-nai (partial denial) / わけがない wake-ga-nai (impossible)
/ わけにはいかない wake-ni-wa-ikanai (mustn't, social) and its negative ないわけにはいかない
nai-wake-ni-wa-ikanai (must), the という-denials というわけ/というものではない (specific inference
vs general principle) + とは限らない to-wa-kagiranai ('not always'), and べきだ beki-da /
べきではない / べきか. Two mandatory look-alike pairs nailed: はずがない≈わけがない (logic vs
conviction) and わけがない≠わけではない (impossible vs not-necessarily). **Batch 9 — こと
decision/outcome/experience (11):** the する/なる decision pair ことにする (own choice) ↔
ことになる (outcome/humble announcement), ことに決める (firmer), the している/なっている pair
ことにしている (personal habit) ↔ ことになっている (external rule), 〜ことだ (hands-on advice,
contra べきだ), ことはない (no-need, consoling), the **ことがある ±た minimal pair** (non-past
= sometimes / past = experience — each contrasts the other), ないことはない (litotes) and the
frozen set phrase に越したことはない (conf med). **No traps this sweep** — variants schema
(`form:`/`note:`) applied correctly throughout. All 1,458 build PASS.

**BUILD common batch 10 DONE (2026-06-15, keigo + こそあど sweep):** two tight clusters in
one turn — 18 nodes, all indexed (299 → **317 indexed**), one consolidated build PASS, lint
clean (18). **Keigo verb family (12):** the suppletive honorifics いらっしゃる irassharu
(いる/来る/行く, irregular いらっしゃ**い**ます) and なさる nasaru (する), their humble mirrors
いたす itasu / いたします itashimasu (する) and さしあげる sashiageru (あげる; 〜てさしあげる
condescension note), くださる kudasaru (くれる; imperative → ください), and the **productive
mirror pair** お〜になる o-ni-naru (sonkeigo) ↔ お〜する o-suru-2 (kenjougo), plus the honorific
request お〜ください o-vmasu-kudasai, the very-polite ございます gozaimasu (ある) / でございます
de-gozaimasu (です copula), and the soft command なさい nasai (← なさる imperative; contra plain
命令形 / 〜てください). Dense register-ladder web: plain→polite→very-polite (ある/あります/
ございます, です/でございます) and the sonkeigo↔kenjougo axis cross-linked throughout. **Trap
avoided:** `mairu` has no node yet — dropped it as a contrast slug (would dangle the build),
kept 参る in restriction prose instead. Note: `o-suru` (N3) is a near-dup stub of the enriched
`o-suru-2` (N4) — left as-is (catalog-level fold decision, out of scope). **こそあど "such /
that kind of" 連体詞 (6):** こういう kou-iu (proximal) ↔ そういう sou-iu (anaphoric) ↔ formal
このような kono-youna, and the question どのような dono-youna (formal ↔ casual どんな donna),
plus the bookish summarizing pair こうした kou-shita ↔ こういった kou-itta. Register ladder
こういう(spoken)→このような/こうした(formal) and emotive こんな contrasted throughout.

**BUILD common batch 11 DONE (2026-06-15, benefactive て-grid + connectives):** three clusters
in one turn — 14 nodes, all indexed (317 → **331 indexed**), one consolidated build PASS, lint
clean (14). **Benefactive て-form grid (7):** the receiving/giving keigo pair ていただく
te-itadaku (humble, on もらう) ↔ てくださる te-kudasaru (honorific, on くれる) — taught as
mirror viewpoints of one event; the request ladder てくれない te-kurenai (casual) ↔
ていただけませんか te-itadakemasen-ka (keigo), with an explicit politeness staircase note
(てくれる？<てくれない？<てもらえますか<ていただけますか<ていただけませんか<ていただけないでしょうか);
the wish pair てもらいたい te-moraitai ↔ てほしい te-hoshii (both contra 〜たい for own action,
both with the ×自分が〜てほしい→行きたい learner-error restriction); and **てやる te-yaru as a
multi-sense node** — ①down-directed benefactive (inferior/animal, condescending if misused) +
②defiant 'I'll damn well do it' (sports/shōnen). Anchored to enriched kureru/ageru/morau/itadaku/
hoshii/tai. **それ-connectives (4):** the result それで sore-de (≈だから but neutral-narrative) vs
concession それでも sore-demo (mirror logic to それで) vs transition それでは sore-de-wa (それじゃ/
じゃあ casual) vs conditional-response それなら sore-nara — all four mutually contrasted on the
real/result vs hypothetical/condition vs concession axes. **"but" connectives (3):** the register
ladder だけど dakedo (casual) → けれど keredo (neutral, +けれども/けど variants, 前置き softening
note) → だが daga (formal/written), cross-linked with が (ga-3), けど (kedo), しかし (shikashi).
**Trap avoided:** `demo` (でも 'but') has no node yet — swapped that それでも contrast to しかし.
Note: `yaru`/`yaru-3` stubs (〜てやる/やる, やる=する) overlap the now-enriched `te-yaru` — left
for a catalog-level fold/disambiguation decision (same situation as o-suru/o-suru-2).

**BUILD common batch 12 DONE (2026-06-19, aspect/phase + causative/passive/potential/perception):**
two clusters in one turn — 29 nodes (26 indexed, 3 noindex colloquial redirects), one consolidated
build PASS, lint clean (29); 331 → **357 indexed**. **Aspect/phase (17):** the compound-verb onset/
continuation/completion set 始める hajimeru ↔ 出す dasu (neutral begin vs sudden burst) ↔ 終わる
owaru ↔ 続ける tsuzukeru; the prep pair ておく te-oku ↔ てある te-aru (doing vs done, with transitive-
only + が-object restriction on てある); the **ところ-phase timeline trio** ているところ teiru-tokoro
(during) ↔ たところ ta-tokoro (just after) ↔ るところだ ru-tokoro-da (about to) — each verb-form picks
a point on the timeline — plus たばかり ta-bakari (subjective recency) contra たところ (objective
moment); the **ていく iku ↔ てくる kuru-2 mirror** (both 2-sense: directional away/toward + change
into-future/up-to-now); ていた te-ita (past of ている); なくなる naku-naru (come to no longer, contra
ようになる); and the colloquial contractions ちゃう chau/ちまう chimau (→てしまう) + とく toku (→ておく)
kept **noindex** as redirect-hubs to dodge the duplicate-content tax. **Causative/passive/potential/
perception (12):** the 五段/一段 causative grid せる seru ↔ させる saseru, the causative-passive
させられる saserareru (put-upon feeling + 飲ます contraction note) and request させてください
sasete-kudasai (contra てください); the **3-way られる homograph** — passive れる reru (五段) /
rareru-2 (一段, already enriched) vs potential られる rareru-3 (が-object, ら抜き note) vs honorific/
spontaneous られる rareru (sonkeigo, lighter than お〜になる) — all mutually disambiguated; られない
rarenai (negative potential); and the **perception confusion** 見える mieru (2-sense: visible / look-
appear) ↔ 見られる mirareru (opportunity-potential) ↔ が見られる ga-mirareru (written 'is observed')
+ 聞こえる kikoeru — the natural-sense (見える/聞こえる, no effort) vs opportunity-potential (見られる/
聞ける, given the chance) split taught explicitly. **Trap caught:** a Hangul 약 slipped into a rarenai
example (약束→約束) — fixed pre-build; the post-batch Hangul scan (가-힣) is now part of QA.

**BUILD common batch 13 DONE (2026-06-19, quotation/report + nominalizers):** two clusters in the
same turn as batch 12, separate consolidated build — 15 nodes, all indexed (357 → **372 indexed**),
build PASS, lint clean (15). **Quotation/report (8):** ということ to-iu-koto (nominalize a whole
statement, ↔ plain こと) ↔ ということだ to-iu-koto-da (**2-sense:** conclusion 'that is to say' /
hearsay 'I hear that', contra そうだ); the **reported-belief trio** mutually contrasted — と言われている
to-iwarete-iru (general unnamed saying) ↔ とされている to-sarete-iru (officially established / rule /
convention, most authoritative) ↔ と考えられている to-kangaerarete-iru (reasoned/expert view, revisable);
と聞いた to-kiita (one-time personal hearsay, can name から-source, ↔ そうだ); と言ってもいい to-ittemo-ii
(hedged 'you could say', + 〜と言っても過言ではない note); and って tte (**2-sense:** casual quotative ≈と /
topic ≈は・というのは). Anchored to enriched という/と-quotative/souda/rashii. **Nominalizers (7):** の
no (**2-sense:** pronoun 'the ~ one' / clause-nominalizer for perceived events, ↔ こと) ・ の-2 (casual
sentence-final explanatory の = だ-dropped のだ, rising=Q falling=soft-explain, feminine note) ・ のこと
no-koto (widen a noun to 'all about', near-obligatory with 好き/愛する/心配する) ・ のは〜だ no-wa-da (cleft
focus, ↔ plain word order & のだ) ・ もの mono (concrete thing ↔ こと abstract) ・ さ sa (adjective→degree
noun 高さ, ↔ ます-stem-noun & 〜み subjective) ・ 連用形名詞用法 masu-stem-noun (動く→動き lexical noun ↔
clause-nominalizers こと/の). Anchored to enriched こと/のだ. **Trap caught (×2):** Hangul autocomplete
slipped into kana examples — 약束→約束 (rarenai, batch 12) and 체조子→調子 (no-2, batch 13) — both fixed
pre-build; a stdlib Hangul scan (가-힣 + Jamo ranges) over each batch is now a standing QA step.

**BUILD common batch 14 DONE (2026-06-19, conditionals):** 12 nodes, all indexed (372 → **384
indexed**), build PASS, lint + Hangul scan clean (12). The high-confusion **negative-copula "unless"
grid** taught by pinning each variant to its conditional base and differentiating: でないと de-nai-to
(と-base, automatic 'or-else' warning) ↔ でなければ de-nakereba (ば-base, neutral, +でなきゃ) ↔ でなくては
de-nakute-wa (ては-base, 'it must be ~', the base of でなくてはいけない, +でなくちゃ) ↔ でなかったら
de-nakattara (たら-base, one-off supposition); plus なかったら nakattara (negative たら for verbs/い-adj,
the copula-form sibling of でなかったら). Other conditionals: のなら no-nara (なら + の, 'taking up what was
said', +んなら) ・ できれば dekireba (fixed adverb 'if possible', softens requests, ↔ できたら) ・ でよければ
de-yokereba (humble offer 'if ~ will do') ・ がなければ ga-nakereba (negative ば of existence ある, 'without';
**bumped low→high conf** — meaning was never shaky, pass-1 artifact; contrast nails existence-vs-identity
がない vs でない) ・ ばいい ba-ii (forward suggestion 'just ~', ↔ たらどう advice & ば〜のに regret, +ばよかった
note) ・ ば〜ほど ba-hodo (proportional 'the more…the more', repeated verb, な-adj→であればあるほど note) ・
ば〜のに ba-noni (counterfactual regret, trailing-のに ellipsis note). Anchored to enriched ば/たら/なら/
と-conditional/なければ-obligation/なくてはいけない/ほど/のに/たらどう. **Note on near-dups:** the four でな-
variants converge on 'unless' but ride genuinely different conditional bases (と/ば/ては/たら), so each is
a legit node, not a fold — differentiation lives in the contrast slot, not in withholding the page.

**BUILD common batches 15–16 DONE (2026-06-19, limitation/exclusion + person-suffixes):** two
clusters, one consolidated build (384 → **406 indexed**, +22), 27 files touched, build PASS, lint +
Hangul scan clean (27). **First action this turn was a recovery:** a prior session had finished
batches 6–14 (192 nodes, frontier+HISTORY advanced) but never committed — verified build+Hangul clean
and committed it as `bfa3425` before starting new work. **Batch 15** (だけ/ばかり limitation + 以外/ほか
exclusion): anchored on bakari, made 2-sense (only/nothing-but ↔ approximate-amount; たばかり time-sense
split off via contrast). The だけ sufficiency/minimum/bottom-line trio dake-de(just by, sufficient
cause)↔dake-demo(even just, worthwhile minimum)↔dake-wa(at least this, non-negotiable) mutually
differentiated; dake-shika↔shika (emphatic double-limiter, negative-required); bakari-de↔dake-de
(positive-result vs negative/no-result). The **"not only but also" pair** だけでなく (everyday) ↔
ばかりでなく (formal/literary) indexed as canonicals and mutually contrasted; the 4 numbered near-dup
seeds (dake-de-wa-naku-2, bakari-de-wa-naku/-2/-4) collapsed to **noindex redirect-hubs** (equiv +
keySentence + contrast→canonical, same treatment as batch-12 chau/chimau/toku). Exclusion: igai(以外)
↔hoka(ほか, +ほかない note)↔hoka-ni-mo; the high-value **同音 以外/意外 trap** igai↔igai-to('unexpectedly')
disambiguated by kanji (以 vs 意); igai-wa→igai redirect. **Batch 16** (person/address suffixes, all 7
indexed): honorific ちゃん(affectionate)↔君(junior/peer)↔様(deferential) laddered against enriched
さん; plural たち(neutral)↔ら(casual/curt)↔方(sonkeigo, *elevates*)↔ども(*humbles/derogates*) — a
politeness-**direction** grid (方 raises others, ども lowers self/others). Fixed kun's seed title
truncated mid-word ("…typically for pee"→"…for juniors and peers"). **Watch (carried to PASS §1):**
the 5 batch-15 redirect-hubs stay noindex and **reappear in `list_stubs --freq common`** — they're
resolved, not pending; skip them.

**BUILD common batches 17–18 DONE (2026-06-19, change-of-state + する-inference connectives):**
two clusters, one consolidated build (406 → **421 indexed**, +15), build PASS, lint + Hangul clean
(15). **Batch 17** (8): the make/become transformation set — くする (transitive 'make ~,' paired
against intransitive くなる) ↔ 化する (formal noun-suffix '-ize,' both trans/intrans by context) ↔
となる (formal 'become,' result-culmination vs everyday になる), anchored to naru/ni-naru/ni-suru;
the sensation/impression sub-cluster — がする (non-visual perception only; restriction: sight uses
見{み}える, not 〜がする) ↔ ような気がする (mental hunch, ↔ ようだ evidence-conjecture) ↔ が気になる
(spontaneous preoccupation; note pairs it with deliberate 気にする); emotion-display がる ↔ たがる
(3rd-person feeling vs verb-desire, restriction: not your own feeling, anchored hoshii/tai). Fixed
ga-suru's truncated seed title ("…feeling occu"→full). **Batch 18** (7): する-based inference/condition
connectives — すると (2-sense: narrative 'thereupon' / inferential 'in that case') ↔ そうすると; the
assumption chain とする (set a premise; note ≠ volitional うとする 'try to') → とすると ('assuming that,'
+とすれば/としたら variants) ↔ からすると ('judging from,' ↔ からみると) ; となると ('when it comes to,'
topical/hypothetical) ↔ になると (literal time/stage change with a regular consequence) — both built
off enriched となる, anchored to と-conditional/なら/tara/ば. Next families flagged in PASS §1:
degree/extent adverbials, 〜場合/〜際 occasion set, or topic/standpoint particles.

**BUILD common batch 19 DONE (2026-06-19, standpoint/means particles + occasion):** one cluster, one
build (421 → **428 indexed**, +7, plus 3 noindex redirects), build PASS, lint + Hangul clean (10).
Standpoint sub-cluster: に関して (formal 'regarding,' ↔ について everyday) ↔ に関する (the adnominal
noun-modifying form, parallel to について↔についての). The by/source/depends triad — による (2-sense:
'due to' noun-modifier / 'depends on' sentence-final) ↔ によって (3-sense: means / passive-agent /
'varies depending on'; the passive-agent sense pinned to rareru-2 as the formal 〜によって描{か}かれた
agent-marker for creation verbs) ↔ によると ('according to [source],' routinely paired with sentence-end
そうだ/らしい hearsay, +によれば variant). Occasion sub-cluster: 際に (formal 'on the occasion of,' ↔ とき
neutral / 場合 hypothetical) ↔ 最中に (the very peak of an ongoing action, almost always interrupted;
restriction: needs an active action, not a static state; ↔ 間に span / ところ moment). Redirects to
enriched anchors: については→ni-tsuite; 場合は & の場合は→baai (the verb-attach and noun-の-attach patterns
of 場合). Fixed ni-yotte/ni-yoru titles to spell out their multi-use senses. Next families flagged in
PASS §1: degree/extent adverbials, 〜以上/〜上で condition-standpoint, ため purpose, or を通して/にとって.

**BUILD common batch 20 DONE (2026-06-19, reason/purpose connectors + grounds/standpoint):** one
cluster, one build (428 → **435 indexed**, +7), build PASS, lint + Hangul clean (7). Reason/purpose
trio: ためだ (2-sense — reason 'it is because' / purpose 'it is for the sake of,' ↔ からだ which lacks the
purpose reading, ↔ わけだ deduction not raw cause) ; そのため ('therefore,' result) ↔ そのために ('to that
end,' purpose) — the bare に flips result→purpose, a clean minimal-pair contrast. 以上 disambiguated by
particle: 以上は ('now that / since,' with obligation/resolve logic in the second clause, ↔ ので plain
cause) vs 以上に ('more than / even more than,' ↔ より basic comparative). 上 disambiguated by **reading**:
〜上で〔うえで〕(2-sense — 'after deliberately doing ~' V-た上で / 'in the course of ~ing' V-る上で, ↔ てから
plain sequence) vs 〜上〔じょう〕('in terms of / from the standpoint of,' fixed compounds 法律{ほうりつ}上,
健康{けんこう}上) — both nodes carry a note pinning the reading split. Fixed a stray typo'd formation key
in ijou-ni pre-build. Next families flagged in PASS §1: degree/extent adverbials, を通して/を通じて, the
たって/ったって concessive-colloquial set, or ことから/ことだから reason-from-grounds.

**BUILD common batch 21 DONE (2026-06-19, こと-reason + までもない idiom + を通して):** one cluster, one
build (435 → **440 indexed**, +5, plus 1 redirect), build PASS, lint + Hangul clean (6). The
grounds-contrast pair: ことから (infer from an observed fact — broken window → burglar; also name-origin
'called X because ~') ↔ ことだから (predict from a person's known character — 'knowing him, he'll be
late'); mutually differentiated on evidence-vs-character, both ↔ ので plain cause. The 言うまでもない
('needless to say') idiom indexed as the frozen instance of the productive 〜までもない ('no need to even
~,' V-plain + までもない, ↔ 必要{ひつよう}はない which lacks the 'overkill/too-obvious' nuance); 〜は言うまでもない
folded to a noindex redirect → 言うまでもない. を通して (2-sense: 'via / by way of' an intermediary ↔
'throughout' a period; +を通じて formal variant; ↔ によって direct means / として role). Fixed を通して's
seeded dangling prereq `o-tsujite` (no such node) → `o`. Next families flagged in PASS §1: degree/extent
adverbials, を通して/を通じて siblings, たって/ったって concessive-colloquial, or ことから/ことだから neighbours.

**BUILD common batch 22 DONE (2026-06-19, verb-completion + capacity/possibility modality):** one
cluster, one build (440 → **447 indexed**, +7), build PASS, lint + Hangul clean (7). A dense
masu-stem aspect/modality web. Completion arc: 〜切る ('do completely / utterly,' quantity 食{た}べ切る
+ intensity 疲{つか}れ切る) ↔ 〜切れない ('can't finish / too many to,' 数{かぞ}え切れない) ↔ 〜かける ('begun
but unfinished' 読{よ}みかけ / 'on the verge of' 死{し}にかける) — 切る vs かける mark the two ends of an action's
arc. Possibility: 〜得る (formal abstract 'it could happen,' read える/うる, restriction: not for learned
skills — 泳{およ}げる not 泳{およ}ぎ得る; ↔ れる/られる concrete ability) ↔ 〜得ない (あり得{え}ない 'impossible';
note the reading stays えない). The headline is the **classic trap pair** 〜かねる ('cannot do ~,' a polite
keigo decline of psychological unwillingness — お答{こた}えしかねます) ↔ 〜かねない ('might (regrettably) do ~,'
undesirable outcomes only — 体{からだ}を壊{こわ}しかねない; restriction: 成功{せいこう}しかねない is wrong, use
かもしれない). Same root かねる, opposite polarity — each node's contrast spells the flip out, with the ない
as the tell. Fixed kaneru's truncated seed title ("…politely decline" missing paren). Next families
flagged in PASS §1: degree/extent adverbials, を通じて siblings, or -ish/tendency suffixes (気味/っぽい/だらけ).

**BUILD common batch 23 DONE (2026-06-19, -ish/tendency/excess suffixes):** one cluster, one build
(447 → **451 indexed**, +4), build PASS, lint + Hangul clean (4). The mutually-confusable
suffix family, differentiated on a degree × time × literal-vs-quality grid: 〜気味 (a slight onset of a
usually-unwelcome state *right now* — 風邪{かぜ}気味, 太{ふと}り気味) ↔ 〜がち (a recurring tendency *over time*,
negative-leaning — 休{やす}みがち, 曇{くも}りがち; freq=uncommon but enriched ahead of band as the 気味 sibling)
↔ 〜っぽい (2-sense: 'resembles / -ish' 水{みず}っぽい / 'prone to' 忘{わす}れっぽい; conjugates like an い-adj;
↔ らしい which is positive 'befitting') ↔ 〜だらけ (a heavy, literal excess, almost always unpleasant —
泥{どろ}だらけ, 間違{まちが}いだらけ; restriction: not for pleasant abundance). Each node's contrasts pin the
specific axis that separates it from the others (気味 slight-now vs がち often-over-time vs っぽい quality
vs だらけ literal-excess). Next families flagged in PASS §1: degree/extent adverbials, を通じて siblings.

**BUILD common batch 24 DONE (2026-06-19, concessive 〜ても emphasis + permission/futility):** one
cluster, one build (451 → **458 indexed**, +7), build PASS, lint + Hangul clean (7). The no-matter-how
trio, differentiated on what each generalises: どんなに〜ても (degree/manner) ↔ いくら〜ても (quantity/repeated
effort; bumped med→high conf) ↔ たとえ〜ても (a hypothetical, often extreme, supposition — 'even if'). どうしても
(2-sense fixed adverb: 'at any cost' / with a negative 'just can't however one tries'). The ても-modality
pair takes opposite stances on the same base: てもかまわない ('it's fine if ~,' permission, ↔ てもいい slightly
more nonchalant) vs ても始まらない ('no use ~ing,' futility). And ても〜なくても ('whether or not,' the binary
yes-case + no-case, vs どんなに's range of degrees). All anchored to enriched te-mo / te-mo-ii. This was
the closing batch of a long session (batches 15–24, +71 indexed nodes: 387→458, all builds green).
Next families flagged in PASS §1: degree/extent adverbials, を通じて siblings.

**BUILD common batch 25 DONE (2026-06-19, sentence-final modal particles):** one cluster, one build
(458 → **467 indexed**, +9), build PASS, lint + Hangul clean (9). Sentence-final modality web: the
wondering pair かな (light casual musing; +negative = a wish) ↔ かしら (the feminine equivalent); na-2
(sentence-final な, emotion / casual agreement — **prohibitive 行くな explicitly disambiguated in a note**)
↔ なあ (the drawn-out, more emotional variant); よね (よ-assertion + ね-confirmation, 'right?'). The
rhetorical 'isn't it?' register pair じゃないか (casual contraction) ↔ ではないか (formal full form, +
volitional 'let us ~'). のだろうか (heavy, introspective 'I wonder' — contrasted as heavier-than-かな,
question-form-of-だろう). だろ (clipped casual だろう → spoken 'right?', register-laddered vs だろう/でしょう).
All anchored to enriched ne/yo/darou/deshou/kamoshirenai/no-2/no-da. Process note: PASS §1 updated this
turn (user directive) — the 20% context ceiling is mine to check between clusters, and I yield the turn
after each build+checkpoint so the hook can re-sample rather than chaining indefinitely.

**BUILD common batch 26 DONE (2026-06-19, hypothetical-outcome evaluation: suggestion/hope/regret/
relief):** one cluster, one build (467 → **473 indexed**, +6), build PASS, lint + Hangul clean (6). The
suggestion register pair たらどう (casual 'why don't you ~') ↔ たらどうですか (polite) — both noted as
directive/potentially-nagging when unsolicited or aimed upward (softer 〜てはいかがですか flagged). The
direction-flip pair: たらどうですか *offers* advice vs たらいいですか (question-word + たらいい) *asks* for it
('what should I ~?'). といい voices a hope about an uncontrolled outcome ('I hope ~', ↔ ばいい advice you
control). The hindsight valence pair ばよかった (regret 'should have ~', +なければよかった 'shouldn't have')
↔ てよかった (relief 'I'm glad I ~', +なくてよかった 'glad I didn't') — explicitly warned not to confuse
なくてよかった (relief) with なければよかった (regret). All anchored to enriched ba-ii/tara/hou-ga-ii/te-mo-ii.

**BUILD common batch 27 DONE (2026-06-19, listing / enumeration particles):** one cluster, one build
(473 → **480 indexed**, +7), build PASS, lint + Hangul clean (7). The exhaustive-vs-representative axis:
や (non-exhaustive noun list 'among others', ↔ と exhaustive) → とか (casual/vaguer; also lists actions/
quotes and hedges a single item; ↔ toka-2 the hearsay とか) → とかとか (explicit example list). など given
2 senses ('and so on' / belittling 〜なんか・なんて), paired with や to close a list. Clause-listing reasons:
し ('and what's more', cumulative grounds toward a conclusion, ↔ から one direct cause) → しし (explicit
multi-reason). もも ('both A and B' / with a negative 'neither nor', ↔ と neutral list & も 'also'; particle-
stacking にも/とも noted). All anchored to enriched to-2/ka/mo/kara/toka-2. Slug trap caught pre-build:
the reason particle is `kara`, not `kara-2` (which doesn't exist) — fixed shi.md's contrast before lint.

**BUILD common batch 28 DONE (2026-06-19, interrogative + でも/も indefinites):** one cluster, one build
(480 → **486 indexed**, +6), build PASS, lint + Hangul clean (6). The affirmative-vs-negative sweep pair:
何でも ('anything', question-word + でも free-choice family 誰でも/どこでも/いつでも) ↔ 何も〜ない ('nothing',
question-word + も + negative). いつ(で)も given 2 senses — いつでも 'any time' (free-choice) vs いつも
'always' (frequency); the で distinguishes them. いくら reworked: a near-dup risk surfaced — いくら〜ても
(`ikura-temo`) and どんなに〜ても (`donna-ni-temo`) were already enriched in batch 24, so `ikura` now leads
with the 'how much?' question word and defers the concessive via cross-ref (no duplicate content). いくら〜でも
given 2 senses (でも-allomorph concessive vs fused いくらでも 'any amount'). でも〜でも ('whether A or B',
↔ も〜も 'both/neither'). Anchored to enriched de-mo/mo/te-mo/donna-ni-temo/ikura-temo. `donnani` (bare)
left a stub by design — donna-ni-temo owns the concessive. New gotcha folded into PASS §1: bare
interrogative adverbs overlap their enriched 〜ても constructions; teach the non-concessive core + cross-ref.

**BUILD common batch 29 DONE (2026-06-19, temporal span connectives):** one cluster, one build
(486 → **492 indexed**, +6), build PASS, lint + Hangul clean (6). 前 done as the noun (2 senses: space
'front' / time 'ago'), with the 'before ~ing' connective left to the already-enriched mae-ni. 前から
('from before / for a while now') as a continuing starting-point, contrasted with 前 (point) and 前に
(one-time event). The core contrast: 間{あいだ}に ('during — at a point within a span'; the に vs bare
間{あいだ} = throughout) ↔ うちに (2 senses: 'while the chance lasts / before it changes' + ているうちに
gradual unplanned change — うちに carries urgency 間に lacks). ているあいだに kept as the ている-attachment
variant cross-referencing 間に (↔ ながら same-subject simultaneity). 間{かん} as the duration suffix
(三時間), reading-split from the あいだ connective explicitly taught. Anchored to enriched
mae-ni/ato-de/nagara/made-ni/te-iru. Slug trap caught pre-build: 'from' から is `kara-3` (kara=reason),
fixed mae-kara's contrast. Dedup handled three 間に faces (aida-ni core / te-iru-aida-ni variant /
no-aida-ni left stub) and the 前-noun vs mae-ni-connective split — same pattern as batch 28's ikura.

**BUILD common batch 30 DONE (2026-06-19, comparison & superlative constructions):** one cluster, one
build (492 → **497 indexed**, +5), build PASS, lint + Hangul clean (5). 方{ほう} resolved from its low
confidence by scoping to the 'the ~ one / side' selection sense — のほうが (`no-hou-ga`, already enriched)
owns the comparison, ほうがいい owns the advice, so 方{ほう} teaches just option-selection (conf bumped
low→med). The two-way vs many-way axis: と〜と、どちらが (compare exactly two; answered by のほうが) ↔
の中で〜が一番 (superlative of three or more; ↔ 一番). の中で sets the group ('among / of all'; で alone
replaces it when the noun is already a whole scope like 世界, から for picking out). ほど〜ない ('not as ~
as', negative-only, mirror of positive より). Anchored to enriched no-hou-ga/yori/ichiban/hodo/hou-ga-ii/de.
Two slug traps caught pre-build: scope で is `de` (not `de-4`), and 'from' から is `kara-3`.

**BUILD common batch 31 DONE (2026-06-19, て-form social/emotional formulas) — 500-INDEXED MILESTONE:**
one cluster, one build (497 → **500 indexed**, +3), build PASS, lint + Hangul clean (3). てね (soft
request/reminder; ね softens the て-form request into 'do ~, okay?'; contrasted with plainer てください and
the pushier てよ; conf bumped med→high). The gratitude-vs-apology pair on the same 'て-form cause + social
reaction' shape: てくれてありがとう ('thank you for ~ing', くれて frames it as a favour done for me) ↔
てすみません (2 senses — apology 'sorry for ~ing' and, since すみません also thanks, 'thank you for the
trouble of ~ing'; なくて for negative cause; formal 〜て申し訳ない/ございません noted). Anchored to enriched
te-form/te-kudasai/kureru/ne. This crosses 500 indexed nodes (from 387 at the start of the 2026-06-19
session — batches 15–31, +113).

**BUILD common batch 32 DONE (2026-06-19, に比べて comparison + と同じ equivalence):** one cluster, one
build (500 → **504 indexed**, +4), build PASS, lint + Hangul clean (4). Extends batch 30's comparison web.
The baseline-comparison near-pair: に比べて (plain 'compared to', a baseline + the gap from it — better for
trends/stats than より which ranks head-to-head) ↔ に比べると (same with the と conditional, 'when one
compares', marginally more tentative). The equivalence pair: と同じで (identical *in kind*; で = copula
て-form leading into a further clause; と違って is its antonym) ↔ と同じくらい (equal *in degree*, 'about as
~ as' — the positive mirror of ほど〜ない). Anchored to enriched yori/hodo-nai/no-hou-ga/gurai/to-2.

**BUILD common batch 33 DONE (2026-06-19, なんか/なんて/なんと colloquial family):** one cluster, one build
(504 → **509 indexed**, +5), build PASS, lint + Hangul clean (5). Follow-on to batch 27's など. なんか
(casual contraction of など, 2 senses: example-cite + belittling; flagged the 何か 'something' homograph
trap). The なんて homograph: citing なんて (re-quotes a word/phrase/**clause** with disbelief/disdain, = などと
contracted) vs exclamatory なんて-2 ('how ~!', heads an adjective *forward*) — same surface, opposite
direction, mutually cross-referenced. なんと given 2 senses: the more-formal 'how ~!' exclamation + the
standalone 'believe it or not' surprise-flag before a fact (flagged the なんとか 'somehow' trap). などと
(など + quotative と, cites speech/thought dismissively; なんて is its casual contraction; ↔ neutral と).
Anchored to enriched nado/toka/to-quotative. Slug trap caught pre-build: 'somehow' is `nan-to-ka`, not
`nanto-ka` — fixed nanto.md's contrast.

**BUILD common batch 34 DONE (2026-06-19, cause/reason connectives with valence):** one cluster, one
build (509 → **514 indexed**, +5), build PASS, lint + Hangul/Cyrillic clean (5). The canonical
valence-contrast pair: せい (noun 'the fault of', negative blame — のせいだ / のせいか hedge / せいにする
'blame on') ↔ おかげ (noun 'thanks to', positive credit — のおかげだ / おかげさまで). Their connective forms
せいで ('because of ~' with an unwanted result, vs neutral から/ので) ↔ おかげで ('thanks to ~' with a good
result) — same shape, opposite valence, mutually contrasted. なぜなら (formal sentence-opener 'the reason
is', pairs with a closing からだ; contrasted with embedded から and result-first だから). Anchored to enriched
kara/node/dakara/tame-da. **QA catch:** a Cyrillic word (благодаря) slipped into okage.md prose during
drafting — caught and removed; the mandatory post-batch scan is now extended to Cyrillic (Ѐ-ӿ) alongside
Hangul (combined regex in PASS §1/§7).

**BUILD common batch 35 DONE (2026-06-19, as-soon-as / the-instant temporal set):** one cluster, one
build (514 → **517 indexed**, +3, plus 1 noindex variant), build PASS, lint + Hangul/Cyrillic clean (4).
たとたん (途端, 'the instant ~') taught as the *past, often unexpected* result that bars commands/plans
in the second clause (↔ literary なり). The base-flip pair on 'as soon as': たらすぐ (たら base → one-off/
planned, freely takes requests and commands) ↔ とすぐに (と base → automatic/habitual, bars commands like
the bare と-result). たらすぐに kept noindex as a trivial に-variant of たらすぐ (just すぐ + optional に — same
duplicate-content reasoning as the redirect-hubs; not worth a separate indexed page). Anchored to enriched
nari/tara/to-conditional/ya-ina-ya/sugu. Fixed to-sugu-ni's prereq suru-to→to-conditional (とすぐに builds
on the と-result, not すると).

**BUILD common batch 36 DONE (2026-06-20, に対して contrast/proportional + result + "speaking-of" topic-shift
+ concessive 〜からといって web):** one cluster-group, one build (517 → **536 indexed**, +19, plus 4 noindex
redirects), build PASS, lint + Hangul/Cyrillic clean (23). Directed by /loop at the に対して/につれて contrast-
and-proportional, その結果 result, and というと/といえば "speaking of" families. に対して taught 2-sense (target
'toward' ↔ contrastive 'whereas', 〜のに対して clause form) ↔ について ↔ 反面 (two opposite sides of the *same*
thing, ↔ ippou-de); につれて proportional gradual change (↔ にしたがって/ば〜ほど; restriction bars commands &
one-time events). Result pair: その結果 (standalone connective ↔ そのため) ↔ 結果 (bound V-た/Nの結果). The
"speaking-of" family mutually cross-linked: といえば (free association) ↔ というと (2-sense +confirmation 'so
that means?') ↔ といったら (2-sense +emphatic 'the sheer ~!') ↔ そういえば (sudden recall, changes subject);
standpoint pair から言うと (conclusion from a basis, ↔ からすると inference) ↔ で言うと (measure/axis rephrase).
The concessive 〜といって web: といっても (concede-then-qualify, canonical) ↔ からといって ('just because', main-
clause-denial restriction) ↔ だからといって (standalone opener) ↔ かといって (rejects the *opposite* alternative)
↔ といって (med-conf: stated-reason/pretext + これといって idiom). かというと set: かというと (Q-then-answer) ↔
なぜかというと (fixed 'the reason is ~からだ', ↔ なぜなら formal). どちらかと言えば softening hedge. Redirect-hubs
(stay noindex, kana/adnominal/full-form dups): ni-taishite-2 (に対する), to-itte-mo (kana といっても), naze-ka-
to-iu-to-kara-da (〜からだ full form), dochira-ka-to-iu-to (と-base). Slug traps: なぜなら=`nazenara`, 反面
contrast=`ippou-de`. Dropped a manufactured に対して contrast on どちらかと言えば (over-fill guard, §2). Anchored
to enriched ni-tsuite/ippou-de/ni-shitagatte/ba-hodo/sono-tame/to-iu/to-naru-to/kara-suru-to/nazenara.

**BUILD common batch 37 DONE (2026-06-20, さえ emphasis/if-only + たって colloquial concessive + 限り
as-long-as + instead-of/despite connectives):** one cluster-group, one build (536 → **545 indexed**, +9, plus
3 noindex redirects), build PASS, lint + Hangul/Cyrillic clean (12). さえ family: さえ ('even', extreme example
↔ も) ↔ でさえ (さえ on a subject noun) ↔ さえ〜ば ('if only', the single sufficient condition ↔ ば). たって
colloquial concessive: たって (た-form+って = casual 〜ても ↔ te-mo) ↔ たって-2 — caught as a REAL separate
construction, not a kana dup: its volitional-form prereq is 〜（よ）うたって 'even if one tries to' (futile
effort), so kept indexed and mutually contrasted with plain たって. 限り 2-sense ('as long as' condition /
'as far as' extent) + ない限り 'unless' note, ↔ 間に time-span. Instead-of/despite set: 代わりに (2-sense
substitute / trade-off-in-exchange ↔ 反面) ↔ くせに ('even though' with reproach, same-subject restriction
↔ のに) ↔ 割には ('considering ~', proportional-expectation mismatch ↔ のに/くせに). Redirect-hubs (stay
noindex, は/の/synonym dups): kagiri-wa (限りは), no-kawari-ni (の代わりに), o-tsujite (を通じて → を通して/
o-toshite, batch-21 enriched). Anchored to enriched mo/te-mo/ba/aida-ni/noni/hanmen/o-toshite.

**BUILD common batch 38 DONE (2026-06-20, degree / frequency / manner adverbials):** one cluster-group,
one build (545 → **553 indexed**, +8, no folds), build PASS, lint + Hangul/Cyrillic clean (8). どんなに scoped
to the non-concessive 'how (much) ~' exclamation/embedded-Q core (どんなに〜ても concessive remains donna-ni-
temo — the bare-vs-〜ても split from batch 28). あまりにも ('far too', emphatic excess ↔ amari). ちゃんと
('properly', casual of きちんと). ごとに ('each/every' ↔ おきに gap-counting / たびに 'each time'). ぶりに
('first time in', 久しぶり note). 一度に ('all at once', いっぺんに note). 再び ('again', formal/written ↔ また
everyday). どうか (med, earnest-plea 'please' ↔ どうぞ offer; 'somehow/whether' sense deferred to its own row).
Flat single-sense adverbs — contrasts only where a real enriched confusable exists; chanto/buri-ni/ichido-ni
left contrast-empty by design (§1 presence-earned, not padded). Anchored to enriched donna-ni-temo/amari/
oki-ni/tabi-ni/mata/douzo.

**BUILD common batch 39 DONE (2026-06-20, だって homograph + では/でも contrastive-particle cluster):** one
cluster-group, one build (553 → **558 indexed**, +5), build PASS, lint + Hangul/Cyrillic clean (5). The だって
homograph pair mutually disambiguated: だって (sentence-initial 'because', casual/defensive, pairs with 〜もん
↔ から neutral) vs だって-2 (particle 'even' on a noun ↔ でも casual equivalent). でもある taught as a parse-trap
(で+も+ある = 'is also', an additional truth, NOT the 'even/but' でも; 〜でもあり〜でもある frame). では = で role-
particle + は contrastive ('in X as opposed to elsewhere', ↔ で neutral / は direct-topic; sentence-initial
では='well then' noted as a separate use). ではなくて = 'not A but B' correction (↔ janai plain negation;
じゃなくて casual variant). Anchored to enriched kara/de-mo/de/janai. Slug notes: では=`de-wa`, じゃない=`janai`.

**BUILD common batch 40 DONE (2026-06-20, まま state set):** one cluster, one build (558 → **559 indexed**,
+1, plus 1 redirect), build PASS, lint + Hangul/Cyrillic clean (2). まま taught 2-sense: 'while left in a state'
(V-た+まま, restriction: た-form required, not dict — 立{た}ったまま not 立{た}つまま; nuance of neglect) vs 'as it
is/unchanged' (そのまま・Nのまま). Contrasts ている (unchanged-with-neglect vs plain progressive) and ないで
(ないまま = lingering-undone state vs ないで links to a following action). ままで folded to redirect → mama (just
まま+で, the で usually droppable). Anchored to enriched te-iru/nai-de.

**BUILD common batch 41 DONE (2026-06-20, ずつ distributive):** one node, one build (559 → **560 indexed**, +1), build PASS, lint + Hangul/Cyrillic clean (1). ずつ ('~ each / at a time', equal amount per unit or step) contrasted with ごとに (unit-focus 'every X' vs ずつ amount-focus). Enriched at the context-budget tail of the session. Anchored to enriched goto-ni.

**BUILD common batch 42 DONE (2026-06-20, simile/'as if' modality + ところ connectives):** one cluster-group, one build (560 → **567 indexed**, +7, plus 1 redirect), build PASS, lint + Hangul/Cyrillic clean (8). Simile set: のような (adnominal 'like ~', modifies a NOUN ↔ youda predicate / youni adverbial) ↔ まるで〜ようだ (vivid 'just like', +neg='completely not') ↔ かのようだ (formal 'as if', explicitly counter-to-fact; combine まるで〜かのようだ). mitaida was already a redirect-hub → mitai, left as-is. ところ connectives: ところで (2-sense 'by the way' topic-shift / V-た+ところで futile 'even if') ↔ ところが ('however', SURPRISING actual result ↔ しかし neutral) ↔ ところに/へ ('right when', interruption at the exact moment ↔ 間に span) ↔ ところだった ('was about to / almost', counterfactual near-miss ↔ るところだ real imminence). ところだ folded to redirect → ru-tokoro-da (batch-12 aspect trio owns the 3-phase). Anchored to enriched youda/youni/mitai/shikashi/aida-ni/ta-tokoro/ru-tokoro-da.

**BUILD common batch 43 DONE (2026-06-20, intention / projection / pretense modality):** one cluster-group, one build (567 → **573 indexed**, +6), build PASS, lint + Hangul/Cyrillic clean (6). 予定だ (fixed arranged schedule, external/objective ↔ つもり personal will). つもり family: つもりで ('with the intention/mindset', adverbial frame ↔ plain つもり predicate) ↔ つもりだった ('had intended but didn't'; with V-た = 'thought I had ~' self-correction). ふりをする ('pretend', intentional act ↔ かのようだ observer-simile — cross-links batch 42). ように+verb projection pair: ように祈る ('pray/hope that', uncontrollable outcome, verb usually potential/intransitive ↔ youni purpose) ↔ ように〜てほしい (med, 'want you to ~ so that ~', purpose-clause + てほしい ↔ bare te-hoshii). Anchored to enriched tsumori/youni/hoshii/te-hoshii/ka-no-you-da.

**BUILD common batch 44 DONE (2026-06-20, difficulty suffixes + span-range particles + compound-verb aspect set):** one cluster-group, one build (573 → **582 indexed**, +10 — enriched-count tool reports 582; the +9 vs +10 gap is a prior counting offset, not a missed flip), build PASS, lint + Hangul/Cyrillic clean (10). **Difficulty pair:** にくい (everyday physical/practical 'hard to ~', i-adj conjugation ↔ enriched やすい exact opposite) ↔ 難い〔がたい〕(literary, psychological/abstract, limited verb set 信じ難い/忘れ難い/表現し難い ↔ にくい register+scope; ↔ かねる polite-decline). **Span-range frame:** にかけて (vague far edge of a range ↔ まで precise endpoint; にかけては 'when it comes to' idiom noted in `notes`) ↔ から〜にかけて (two fuzzy edges ↔ から〜まで exact boundaries via kara-3). **Compound-verb aspect set:** 上がる・上げる (finish to a produced result; intransitive/transitive pair documented in `notes`; ↔ 切る exhaust-quantity ↔ 終わる neutral-stop) · 合う (reciprocal 'to each other', plural/mutual-subject restriction, ↔ 続ける; お互いに + standalone-合う 'fit' in `notes`) · 込む (**2-sense**: ①inward 乗り込む/詰め込む ②thoroughly 考え込む/話し込む; ↔ 切る) · 直す (redo-to-correct, first-try-flawed restriction; もう一度 neutral-repeat + standalone 直す 'repair' in `notes`) · 通す (sustain one stance to the end 押し通す/守り通す; ↔ 抜く hardship vs ↔ 切る complete) · 抜く (push through *hardship* to the end 耐え抜く/生き抜く; ↔ 通す consistency vs ↔ 切る neutral; standalone 抜く 'extract'/手を抜く idiom in `notes`). Anchored to enriched yasui/kaneru/made/kara-3/kiru/owaru/tsuzukeru. **Missing anchors handled as prose notes, not dangling contrasts** (tagai-ni, deru, uru absent from catalog — お互いに/standalone-verb caveats routed to `notes`). The three clusters the resume directive named are now drained.

**BUILD common batch 45 DONE (2026-06-20, temporal after/since/before/during + もの/もん modality + conjecture/likelihood modality):** one cluster-group, one build (582 → **597 indexed**, +15), build PASS, lint + Hangul/Cyrillic clean (15). **Temporal set:** 以後〔いご〕(boundary 'from then on' + standalone 'henceforth' corrective tone) ↔ 以降〔いこう〕(range marker, needs time anchor) ↔ 以来〔いらい〕(past point→present, continuous, ↔ kara-3) · ないうちに ('before an unwanted change', urgency ↔ 前に; ↔ affirmative うちに opposite-side) · 中〔ちゅう〕(に) (2-sense in-the-middle/within-a-period; じゅう='throughout' note; ↔ aida-ni/made-ni) · の間に (Nの variant of 間に; ↔ aida-ni/te-iru-aida-ni). **もの modality:** ものだ (2-sense general-truth/social-norm 'should' + ものではない 'shouldn't'; ↔ beki-da specific vs general, ↔ hazu-da deduction vs norm) ↔ たものだ ('used to', nostalgic ↔ ていた) ↔ もん (casual self-justifying excuse, だって〜もん; ↔ から/datte). **Conjecture certainty-scale:** に違いない (firm 'must be', ↔ hazu-da/kamoshirenai/darou) ↔ 考えられない (firm 'unthinkable', opposite pole, ↔ enai) · だろうか ('I wonder', ↔ darou/kana) · 可能性がある (objective gradable, ↔ kamoshirenai subjective, ↔ osore-ga-aru risk-only) · そうにない (neg appearance そう, ↔ souda-2) ↔ そうになる ('almost'/near-miss, ↔ tokoro-datta/kakeru). **Prereq fix:** sou-ni-nai souda→souda-2 (appearance, not hearsay); sou-ni-naru += souda-2. **Confidence bumps:** igo/ikou/chu-ni med→high (standard meanings, cleared gate). **Homograph trap navigated:** souda (hearsay) vs souda-2 (appearance) — the sou-ni-* nodes belong to souda-2. Anchored to enriched ato-de/mae-ni/aida-ni/te-iru-aida-ni/made-ni/kara-3/uchi-ni/mono/beki-da/hazu-da/te-ita/kara/datte/kamoshirenai/darou/kana/osore-ga-aru/souda-2/tokoro-datta/kakeru/enai.

**BUILD common batch 46 DONE (2026-06-20, can't-help/unbearable + から standpoint + から reason-emphasis + only/limitation):** one cluster-group, one build (597 → **614 indexed**, +17), build PASS, lint + Hangul/Cyrillic clean (17). **Can't-help family:** たまらない (standalone; +positive 'irresistible' note) ↔ てたまらない (sharp/physical) ↔ てしかたがない (everyday; てしょうがない casual) ↔ てならない (literary, feelings only); 仕方がない (resignation 'can't be helped' vs てしかたがない 'can't help feeling' — same chars, opposite function); ならない (**disambiguation hub**: feeling てならない vs obligation なくては/ねば+ならない). **から standpoint quartet** (off enriched kara-suru-to/kara-iu-to): から見て ↔ から見ると (て-vs-と viewpoint-shift) ↔ からして ('even from just X' + 'to say nothing of rest') ↔ から言って (criterion/standard, ↔ から言うと). **から reason-emphasis:** からこそ ('precisely because'+のだ) ↔ からには ('now that', resolve main clause, ↔ ijou-wa) ↔ からだ (sentence-final reason, pairs なぜなら, ↔ wake-da). **only/limitation:** しかない (2-sense no-choice/only, ↔ yori-hoka-nai) ↔ でしかない ('merely', ↔ ni-suginai) ↔ きり (2-sense 'only'/V-た+きり 'and then nothing' 寝たきり, ↔ dake/shika) ↔ たった ('a mere', number-only, ↔ dake/wazuka). **Confidence bumps:** shikata-ga-nai low→high (clear common phrase), kara-shite med→high; naranai kept med w/ review_reason (bound-element hub). **te-shou-ga-nai stays noindex** — folded as variant note on te-shikata-ga-nai (redirect candidate). Anchored to enriched kara/kara-3/kara-suru-to/kara-iu-to/node/wake-da/nazenara/ijou-wa/shika/dake/wazuka/ni-suginai/yori-hoka-nai/nakereba-naranai/te-ita.

**BUILD common batch 47 DONE (2026-06-20, 向け/向き suitability-vs-intent pair):** small tail batch near context ceiling (614 → **616 indexed**, +2), build PASS, lint + Hangul clean (2). 向け ('deliberately made/aimed FOR a target', maker's intent) ↔ 向き (2-sense: 'naturally suited to' + literal 'facing'; 前向き/後ろ向き idiom note) — classic confusable pair on the intent-vs-suitability axis. Self-contained pair (no enriched sibling anchor).

**BUILD common batch 48 DONE (2026-06-20, 自分/自身 reflexive pair):** tail batch (616 → **618 indexed**, +2), build PASS, lint + Hangul clean (2). 自分 (standalone reflexive pronoun 'oneself', subject-bound; humble-'I' note) ↔ 自身 (emphatic suffix on noun/pronoun 'that very ~'; combine 自分自身) — standalone-pronoun vs bound-emphatic-suffix axis. Both bumped med→high.

**BUILD common batch 49 DONE (2026-06-20, N5 high-priority basics — が-predicates + basic verbs + particles):** 618 → **628 indexed** (+10), build PASS, lint + foreign-script scan clean (10). Raised the context_gate Stop-hook threshold 200k → 250k per user directive. のが上手 ↔ のが下手 (mutual good/bad-at pair, Vる+のが+な-adj; 得意 vs 上手, 苦手 vs 下手 notes); 好きだ (が-object-not-を restriction ↔ 欲しい obtain); 要る (u-verb-despite-る + が-object ↔ 必要がある); 知る (punctual asymmetry 知っている/知らない ↔ ている resulting-state; vs 分かる); か-2 ('or', added examples ↔ ka); に-4 (passive/receiving agent; created-thing → によって restriction ↔ から); を使って (means ↔ で/によって); どうぞ (offer/invite ↔ どうか plea, vs どうも). Bumps: iru-4/sukunai low→high, shiru/sukida/o-tsukatte med→high. Fixed sukida truncated seed title.

**BUILD common batch 50 DONE (2026-06-20, N4 material/particle/conditional basics):** 628 → **637 indexed** (+9), build PASS, lint + foreign-script scan clean (9). でできる ('made of', visible material ↔ から作る) ↔ から作る ('made from', transformed; fixed truncated title) — で/から split; を-2 (path 道を歩く ↔ で location) ↔ を-3 (departure 家を出る ↔ から-3, ↔ を-2) off を object; も-2 ('even' ↔ さえ / も additive; number+も restrictions); なくても ('even if not' ↔ ても; なくてもいい note); か〜か ('whether or' ↔ か〜ないか / か-2); もし(も) ('if' adverb — only signals the conditional, restriction ↔ たら); 少なくない (litotes ↔ 少ない). All anchors enriched.

**BUILD common batch 51 DONE (2026-06-20, N4 remainder grab-bag — drains N4 common band):** 637 → **649 indexed** (+12), build PASS, lint + foreign-script scan clean (12). いい (irregular よ-stem restriction; declining-tone note); いかが (polite ↔ どう); 命令形 (imperative reference page ↔ てください/なさい); 自動詞・他動詞 (intransitive/transitive reference, が/を restriction ↔ てある); 真っ〜 (non-productive intensifier prefix); 〜目 (ordinal ↔ 番目); んだけど (softening preface ↔ kedo/no-da); に気がつく (に not を ↔ が気になる; 気づく syn); おい (rough male 'hey!'); と一緒に (↔ to-2); 〜は〜の一つだ ('one of the' pattern); ところ (2-sense base nominalizer — kept distinct from the ところだ aspect trio, routes to ru-tokoro-da + sub-construction pages). Bumps: ii/jidoushi-tadoushi low→high, me med→high. **N4 common band drained; next is N3 common.**

**BUILD common batch 52 DONE (2026-06-20, N3 common opener — もしも conditionals + か whether/or + こそ/reason + み/面 suffixes):** 649 → **659 indexed** (+10), build PASS, lint + foreign-script scan clean (10). もしも〜なら (premise ↔ もしも〜たら) ↔ もしも〜たら (event-result sequence) off batch-50 もし(も); か〜ないか ('whether or not', repeat-verb ↔ か〜か; かどうか syn) · か何か ('or something' hedge ↔ とか) · または (formal 'or' ↔ か-2; それとも/あるいは); こそ ('precisely', replaces は/が ↔ からこそ; fixed title) · のだから ('because as-you-know' → assertion ↔ から) · なぜか ('for some reason' ↔ なぜなら, opposite jobs); み ('-ness', non-productive ↔ さ productive — THE pair; fixed title) · 面 ('in terms of' ↔ 上 domain). N3 common band opened.

**BUILD common batch 53 DONE (2026-06-20, N3 common — にしても/にしては + prohibition + こと-connectives + rather/somehow):** 659 → **667 indexed** (+8), build PASS, lint + foreign-script scan clean (8). にしても ('even granting' ↔ にしては) ↔ にしては ('for/considering', concrete-standard restriction ↔ 割には wari-ni-wa); 〜な (rough 'don't' ↔ 命令形/na-2) ↔ ないようにしてください (polite ↔ てはいけない); ことで ('by ~ing' ↔ て; のことで/ということで disambig; med→high) · 〜ことは〜が ('admittedly but', repeat-word); むしろ ('rather' ↔ というより) · なんとか ('somehow=manage' ↔ batch-52 なぜか 'somehow=cause' — the trap). Slug trap caught: 割には = wari-ni-wa.

**BUILD common batch 54 DONE (2026-06-20, N3 common — に-based connectives + 'without' pair):** 667 → **674 indexed** (+7), build PASS, lint + foreign-script scan clean (7). に当たる ('correspond to'; にあたって/literal-hit note; med→high) · に合わせて ('adjust to match' ↔ にしたがって) · によれば ('according to' ↔ によると, formal-vs-spoken) · に慣れる ('get used to', に-not-を; 慣れている/慣らす) · に限る ('nothing beats', subjective ↔ ほうがいい; disambig 限る/に限らず/に限って); なしで (noun 'without' ↔ ないで verb) ↔ なく (formal continuative neg ↔ ないで/ずに; med→high). Bumps: ni-ataru/naku med→high.

**BUILD common batch 55 DONE (2026-06-20, N3 common — report/obvious/concession/purpose + adverbs):** 674 → **680 indexed** (+6), build PASS, lint + foreign-script scan clean (6). んだって (casual hearsay ↔ そうだ) · 当たり前だ ('only natural' ↔ ものだ) · ながらも ('although' ↔ ながら/のに) · には ('in order to' purpose ↔ ために; med→high) · 一般に ('generally' ↔ 普通) · なるほど ('I see', superior-caution). Bump: ni-wa med→high. Session batches 49–55: 618 → 680 (+62).

**BUILD common batch 56 DONE (2026-06-20, N3 common — casual final particles + listing/additive):** 680 → **685 indexed** (+5), build PASS, lint + foreign-script scan clean (5). だい (masculine wh-question ↔ ka/かい; fixed title) · っけ (recall '...was it?', past form ↔ ka) · 何〜も ('as many as' ↔ mo-2; vs 何も+neg; med→high) · などの ('such as' ↔ など) · あと ('and also' casual ↔ それに; vs 後で/remaining; med→high). Bumps: nan-mo/ato med→high. **Session batches 49–56: 618 → 685 (+67); N4 common band drained, deep into N3 common; context_gate threshold raised 200k→250k.**

**BUILD common batch 57 DONE (2026-06-20, N3 common tail):** 685 → **688 indexed** (+3), build PASS, lint + foreign-script scan clean (3). と関係がある ('related to' ↔ に関して) · もともとの ('original' adnominal; med→high) · 一方だ ('keeps getting worse', one-way trend ↔ ていく; disambig 一方で/noun; med→high). Bumps: motomoto-no/ippou-da med→high. **Session batches 49–57: 618 → 688 (+70).**

**BUILD common batch 58 DONE (2026-06-20, N3 common — discourse connectives + modality/question/particle grab-bag):** working-tree indexed 669 → **698** (+29 indexed + 1 noindex redirect), build PASS, lint clean (30), Hangul/Cyrillic scan clean. (Count reconciled to actual grep: frontier had been tracking 688; the working tree's true indexed total was 669 pre-batch, so this lands at 698.) **Cluster 1 (というX定義/言い換え + それ-connectives + discourse openers + temporal/degree adverbs, 17 indexed + 1 redirect):** というのは (2-sense definition 'X means' / reason 'the reason is', ↔ つまり/ということは) · という理由で (formal stated grounds, ↔ から) · というふうに (cite a manner/example 'in such a way', ↔ ように) · つまり (restate-as-conclusion 'in other words', ↔ というのは/要するに) · というより (reject first label for an apter one, ↔ むしろ pair / より degree) · それと (tacked-on extra item, ↔ それに reinforcing / そして sequence) · それとも (alternative-question 'or', ↔ か-2 phrase-level / あるいは formal) · そこで (deliberate action in response, ↔ だから result / それで; **conf med→high**) · さあ (2-sense prompting 'come on' / hesitation 'hmm', ↔ さて) · さて (topic-shift 'now then', ↔ つまり/そこで) · せいぜい (upper-limit 'at most', dismissive, ↔ せめて minimum-hope) · しばらく ('for a while'; しばらくですね long-gap greeting note) · つい (2-sense lapse-against-self-control / 'just now', ↔ 思わず reflexive / うっかり careless) · ついでに (secondary task on the same errand, ↔ ながら simultaneous) · 通りに (exact match to a model 'just as', ↔ ように manner-goal / まま unchanged; 〜どおり fusion note) · 途中で (midway/on-the-way, ↔ 間に span) · 例えば ('for example', flat). **totan-ni (途端に) → noindex redirect-hub → ta-totan** (batch-35 owns 途端). **Cluster 2 (modality/seeming + softened/rhetorical question + particle/difficulty grab-bag, 12 indexed):** と言える (warranted conclusion 'one can say', ↔ だろう conjecture; とは言えない note) · とみえる (infer from observed evidence, ↔ ようだ everyday / らしい hearsay; fixed truncated title) · のでしょうか (polite softened 'I wonder', ↔ のだろうか plain) · たらいいか (question-word 'what should I ~?', ↔ ばいい states-advice) · 反語 rhetorical-question (reference page: question-shape = forceful opposite assertion, ものか/だろうか, ↔ だろうか; fixed truncated title) · ただ (2-sense 'only/just' / caveat 'however', ↔ だけ particle / しかし full-contrast; ただし note) · ときには ('at times', exception-to-usual, ↔ たまには) · たまには ('once in a while / for a change', treat-yourself, ↔ ときには) · てごらん (gentle superior→inferior 'try ~ing', ↔ てみる neutral / なさい firmer; usageSetting) · づらい (doer's-discomfort 'hard to', ↔ にくい objective / 難い literary) · ぞ (rough masculine forceful-assertion/resolve, ↔ よ inform; ぜ note) · ずに (formal 'without ~ing', せずに irregular restriction, ↔ ないで spoken / なく formal-link). **Confidence bumps:** soko-de med→high, tada med→high (meanings standard, gate cleared). **Fixed truncated/malformed seed titles:** to-mieru, rhetorical-question.

**BUILD common batch 59 DONE (2026-06-20, N3 common — として family + purpose/projection ように + concession + を-connectives + interval/state/reason):** 698 → **719 indexed** (+21), build PASS, lint clean (21), Hangul/Cyrillic scan clean. **として family:** として (role 'as') ↔ としては (standpoint/yardstick, ↔ にしたら) ↔ としても (N2 hypothetical 'even if', ↔ ても/にしても; med→high). **purpose ように:** ように言う (indirect command, ↔ と言う; med→high) · のに-2 (purpose のに, dict-form+cost/便利, disambig from concessive のに; med→high) · ようとしない (↔ ようとする). **concession:** 確かに〜が (self-raised; med→high) ↔ そうですが (dialogue reply; med→high) · は (contrastive/emphatic advanced は, ↔ が/も; med + review_reason). **を-connectives:** を込めて · をはじめ(として) (↔ など) · を左右する (med→high). **interval/state/reason:** おきに (↔ ごとに; 一日おきに='every other day' trap) · っぱなし (2-sense neglect/continuous, ↔ てある) · て済む (↔ ずに済む) · てからでないと (↔ てから) · ている場合じゃない (↔ どころではない) · おかげで (positive twin of せいで, ↔ から) · まるで (pairs ようだ, +neg='completely not') · 行う (formal, ↔ やる; low→med) · 〜的 (↔ 風に). **Dangling-slug fix:** okonau contrast suru→yaru (no standalone する node). Bumps: to-shite-mo/youni-iu/noni-2/tashika-ni-ga/so-desu-ga/sayuu-suru med→high, okonau low→med.

**BUILD common batch 60 DONE (2026-06-20, N2 common opener — という family + もの modality + emphatic total-negation):** 719 → **731 indexed** (+12 indexed + 1 noindex redirect), build PASS, lint clean (13), foreign-script scan clean (after fix). **emphatic negation:** 一切〜ない (categorical, ↔ まったく) · ろくに〜ない (inadequate+complaint, ↔ まったく) · なくはない (double-neg partial-yes, ↔ わけではない). sukoshi-mo-nai already redirect→sukoshi-mo, skipped. **という family:** ということは (forward-inference, ↔ つまり/というのは) · というか (self-correction 'or rather', ↔ というより) · とは (2-sense definition/surprise; med→high) · というのに (emotional 'even though', ↔ のに) · というものだ (emphatic verdict, ↔ ものだ). **もの modality:** ものの (written concession, ↔ のに/とはいえ) · ものだから (excuse 'because you see', ↔ から/ので) · ものですから → noindex redirect → mono-dakara (fixed truncated title) · ものがある (felt-impression, ↔ ものだ) · ものではない (social-norm 'shouldn't', ↔ べきだ). **QA catch:** stray Cyrillic 'ків' in mono-de-wa-nai reading caught by foreign-script scan, fixed pre-build. Bump: to-wa med→high.

**BUILD common batch 61 DONE (2026-06-20, N2 common — に-compound families: basis/according-to + regardless/contrary + direction):** 731 → **744 indexed** (+13 indexed + 3 noindex redirects), build PASS, lint clean (16), foreign-script scan clean. **basis/according-to:** に基づいて (binding standard) ↔ をもとに (raw-material/springboard) · に沿って (2-sense along/conformity, ↔ に従って) · に応じて (vary-with) ↔ に応えて (live-up-to; 応 reading trap おうじる/こたえる) · に伴って (accompanying change, ↔ につれて/に従って). **regardless/contrary:** に反して (violates expectation, ↔ に対して) · に反する → redirect → ni-hanshite · にかかわらず ↔ にもかかわらず (THE も-pair: regardless-of-variable vs in-spite-of-fact) · を問わず (category, ↔ にかかわらず) · に限らず ('not limited to', ↔ だけでなく) · にも関わらず → redirect → ni-mo-kakawarazu (kanji). **direction:** に向かって (physical, ↔ へ) ↔ に向けて (goal/audience) · に向けて／向けた → redirect → ni-mukete (adnominal). **Slug trap:** だけでなく = dake-de-wa-naku (caught at lint, dake-de-naku missing). **QA catches:** bogus attaposed key in o-moto-ni removed; duplicate ni-mukatte contrast in ni-mukete de-duped. **Session batches 58–61: 669 → 744 (+75 indexed).**

**BUILD common batch 62 DONE (2026-06-20, N2 common — additive 'moreover' connectives + natural/certainty modality):** 744 → **754 indexed** (+10 indexed + 4 noindex redirects), build PASS, lint clean (14), foreign-script scan clean. **additive (same-direction 'on top of that'):** に加えて (noun-attach, ↔ その上) · その上 (sentence-connector, ↔ しかも) · その上に → redirect → sono-ue · さらに (2-sense addition/'even more') · しかも (additive + striking, ↔ その上/さらに) · おまけに (casual, piles-on) · 上に〔うえに〕 (clause-attach, disambig 上で/上じょう) · および (formal listing 'and', ↔ と). **natural/certainty:** 当然だ (canonical, ↔ 当たり前だ/はずだ; med→high) ← て当然だ/も当然だ/のも当然だ → redirect → touzen-da · に決まっている (emotional 'obviously', ↔ に違いない/はずだ; low→high) · っこない (casual 'no way', ↔ わけがない). Redirect-hubs: sono-ue-ni, mo/no-mo/te-touzen-da. Clean batch, no QA slips. **Session batches 58–62: 669 → 754 (+85 indexed).**

**BUILD common batch 63 DONE (2026-06-20, N2 common — を-scope/focus/exception + と-simultaneity/listing + どころ-contrast):** 754 → **764 indexed** (+10), build PASS, lint clean (10), foreign-script scan clean. **を-scope:** をめぐって／めぐる (contested issue, ↔ について; med→high) · を中心として／に (focal point, ↔ をめぐって; med→high) · を除いて (formal except, ↔ 以外) · 抜きで (without a normal inclusion, ↔ なしに) · 自体 (things 'itself', ↔ 自身 people; med→high). **と-simultaneity/listing:** とともに (2-sense accompaniment/parallel-change, ↔ と同時に) ↔ と同時に (2-sense same-instant/two-facets, ↔ とともに/ながら) · といった ('such as'→category, ↔ など/や). **どころ pair:** どころか (reverses expectation 'far from', ↔ かえって) ↔ どころではない ('no room for', ↔ どころか/ている場合じゃない). Clean batch, no QA slips. Bumps: megutte-meguru/o-chushin-to-ni-shite/jitai med→high. Deferred: to-iu-youna/youni (overlap といった). **Session batches 58–63: 669 → 764 (+95 indexed).**

**BUILD common batch 64 DONE (2026-06-20, N2/N3 common — discourse connectives + は-topic restriction + risk/tendency modality + degree-limiting):** 764 → **782 indexed** (+18), build PASS, lint clean (18), foreign-script scan clean. **discourse connectives:** それに ('besides', same-direction add, ↔ そして/その上/それなのに) · それなのに ('and yet', reproachful contradiction, ↔ のに/それにしても/しかし) · それにしても ('even so', half-concede+marvel, ↔ それなのに/とにかく) · 逆に ('conversely', genuine reverse, ↔ かえって/むしろ) ↔ かえって ('on the contrary', ironic backfire, ↔ 逆に/むしろ) · 要するに ('in short', boil-down, ↔ つまり) · 従って (formal 'therefore', ↔ だから/要するに; に従って homograph disambig) · ちなみに ('incidentally', related aside, ↔ それに) · あるいは (formal 'or', ↔ または/それとも). **は-topic restriction:** はともかく ('setting aside', casual-dismissive, ↔ は別として) ↔ は別として ('apart from', neutral-defer +〜かどうか, ↔ 以外) · はもちろん ('A of course, B too', ↔ だけでなく/はもとより) ↔ はもとより (formal twin, ↔ はもちろん/だけでなく). **risk/tendency modality:** 傾向がある (neutral 'tends to', ↔ がち/やすい) · 危険性がある (clinical 'risk', ↔ 恐れがある/可能性) ↔ 恐れがある (forecast 'danger', negative-only, ↔ 可能性/危険性). **degree-limiting:** に過ぎない ('no more than', dismissive, ↔ だけ/単に) ↔ 単に ('simply', wants closing だけ/に過ぎない; 単なる before nouns, ↔ ただ). Slug notes: または=mata-wa, しかも=shika-mo. Self-contrast caught (wa-tomokaku→notes). Clean build, no QA slips.

**BUILD common batch 65 DONE (2026-06-20, N2 common — ては warning/prohibition + only-after/by emphatic + "without" set + formal に scope/span + standpoint/accordance に + increasing-degree adverbs):** 782 → **799 indexed** (+17), build PASS, lint clean (17), foreign-script scan clean. **ては:** ては ('if→bad result', ちゃ/じゃ contractions, ↔ と/てはいけない) ↔ ていては ('keep ~ing→bad', ↔ ては/ている) · てはならない (formal 'must not', ↔ てはいけない/ては). **only-after/by:** てはじめて ('only after', realisation, ↔ てから/てこそ) ↔ てこそ ('only by ~ing', necessary means, ↔ からこそ/こそ). **without:** なしに (noun-based formal, ↔ ないで/ことなく) ↔ ことなく ('not even once', dict-form, ↔ ないで/なしに) ↔ ずに済む ('get by without', せずに済む, ↔ ずに/ないで). **formal に scope/span:** において (formal place/domain, における adnom, ↔ で) · にわたって (full-coverage span, にわたる adnom, ↔ にかけて/まで) · につき (2-sense per/due-to; disambig について). **standpoint/accordance:** にしたら (person's viewpoint, にすれば/にしてみれば, ↔ にとって/からすると) · に従って (2-sense obey-rule/proportional, 従い formal, homograph 従って; ↔ につれて/に応じて). **degree adverbs:** ますます (trend snowballing, ↔ 一層/さらに) ↔ 一層 (deliberate step-up, より一層, ↔ ますます/もっと) · よほど (inferred degree+conjecture, よっぽど, ↔ かなり/あまり) · 実に (heartfelt eval; disambig 実は, ↔ 本当に/とても). Slug note: に応じて=ni-oujite. Clean build, no QA slips.

**BUILD common batch 66 DONE (2026-06-20, N2 common — manner/likeness という set + superlative/at-any-rate + concessive even-if/despite + evaluative/degree adverbs + almost/somehow/carelessly):** 799 → **817 indexed** (+18, +1 redirect), build PASS, lint clean (19), foreign-script scan clean. **manner/likeness:** 風に (colloquial style, 〜風 noun-suffix, ↔ ように) ↔ という風に (cite clause as manner, ↔ 風に/というように) · というように (manner/example-pattern/'as if to say', adverbial, ↔ といった/というような) ↔ というような ('such ~ as', adnominal→NOUN, ↔ といった/というように) · かのように ('as if' counter-to-fact, まるで〜, ↔ かのようだ/ように). **superlative/at-any-rate:** 何より ('more than anything', ↔ 一番/何といっても) ↔ 何といっても ('above all', ↔ 何より/とにかく) · 何しろ ('after all, you see', なにせ/なんせ, ↔ とにかく) ← なにしろ kana→noindex redirect→nani-shiro. **concessive:** であっても (formal 'even if it is', N/な-adj, ↔ でも/ても) · くせして ('even though'+reproach, casual くせに, same-subject, ↔ くせに/のに) · もかまわず ('heedless of', 構う-neg, ↔ にもかかわらず). **degree adverbs:** 案外 ('unexpectedly', ↔ 意外と; med→high) · 幸い ('fortunately'; 〜ば幸いです request) · 少なくとも ('at least', ↔ せめて/せいぜい) · わずかに ('slightly', ↔ わずか). **almost/somehow/carelessly:** もう少しで ('almost', near-miss, ↔ ところだった/そうになる) · どうにか ('somehow manage', ↔ なんとか/どうか) · うっかり ('carelessly', lapse, ↔ つい; med→high). Bumps: angai/ukkari med→high. というような(→N) vs というように(→V) split taught. Clean build, no QA slips. **Session batches 64–66: 764 → 817 (+53 indexed).**

**BUILD common batch 67 DONE (2026-06-20, N2 common — inference/seeming/opinion modality + wish + hearsay):** 817 → **822 indexed** (+5, +1 redirect), build PASS, lint clean (6), foreign-script scan clean. 思われる (spontaneous れる 'it seems/is thought', impersonal-formal, ↔ と考えられる/れる・られる; med→high) ↔ と考えられる (reasoned conclusion, ↔ と考えられている/思われる) · のではないだろうか (softened assertion-as-question, のではないでしょうか polite, ↔ のだろうか/じゃないか) · たらいいのに ('I wish but isn't so', regret-のに, ↔ ばいい/ばよかった/といい) · とか(で) (sentence-end hearsay/vague, distinct from listing とか, ↔ そうだ/って/とか; med→high). te-shou-ga-nai (てしょうがない)→noindex redirect→te-shikata-ga-nai (resolves batch-46/58 fold candidate). Bumps: omowareru/toka-2 med→high. と考えられる(analytic) vs 思われる(impression) split taught. Clean build, no QA slips. **Session batches 64–67: 764 → 822 (+58 indexed).**

**BUILD common batch 68 DONE (2026-06-20, N1 common — 'in one's own way' appropriate-to-nature + irreversible-state adverb):** 822 → **824 indexed** (+2, +2 redirects), build PASS, lint clean (4), foreign-script scan clean. なりに ('in one's own way / suited to level', modest-effort-within-limits; adverbial なりに / adnominal なりの both taught; それなりに note; ↔ らしい) ← なりに／なりの (nari-ni-no)→noindex redirect→nari-ni · もはや (formal 'by now/no longer', irreversible, ↔ もう). のことだから (no-koto-da-kara)→noindex redirect→koto-dakara (canonical full form of ことだから, batch-21 enriched — dedup fold). Clean build, no QA slips. **Session batches 64–68: 764 → 824 (+60 indexed).**

**BUILD common batch 69 DONE (2026-06-20, N3 common — distributive 'each'):** 824 → **825 indexed** (+1), build PASS, lint clean (1), foreign-script scan clean. それぞれ ('each / respectively', individual distinctness within a group; それぞれの+N; ↔ ずつ equal-share / ごとに per-unit; めいめい/各自 synonym note). Single-node batch at context ceiling. Clean build, no QA slips. **Session batches 64–69: 764 → 825 (+61 indexed).**

**BUILD common batch 70 DONE (2026-06-21, mixed common grab-bag — approximation/portion particles + aspect/sequence + contrast + adverbials + basis/dependency connectives + 'some-kind-of'):** 825 → **842 indexed** (+17), build PASS, lint clean (20), foreign-script scan clean. 3 redirects (kurai→gurai, to-iu-yori-wa→to-iu-yori, nani-ka-no→nanraka-no). Approximation/portion: あたり (around a point ↔ ごろ/ぐらい) · 分 (corresponding share ↔ ぐらい; その分 note) · のうち(で) (select-from-set ↔ の中で/うちに). Aspect/sequence: かと思うと (no-sooner-than, speaker-observed ↔ た途端/や否や) · つつある (change-in-progress, formal ↔ ている) · た末(に) (effortful-process→outcome ↔ た途端/後で; あげく note). Contrast: 一方(で) (coexisting facts ↔ 反面/に対して; **一方だ disambiguated**) · いわゆる (so-called, 連体詞). Adverbials: 万が一 (remote serious possibility ↔ もし(も)) · あらかじめ (beforehand, formal) · 何から何まで (everything, から〜まで frame). Basis/dependency: にかかっている (hinges-on ↔ によって) · を踏まえて (weigh-prior-facts ↔ に基づいて/をもとに) · がきっかけで (triggering incident ↔ によって) · に関わる (grave-matter ↔ について) · いずれにしても (either-way ↔ とにかく). Some-kind-of: 何らかの (adnominal asserts-existence; なにかの reading variant). **QA catches:** dropped self-referential empty contrast (ni-kakatteiru); moved 何か comparison to notes (nani-ka absent); fixed duplicate `confidence:` key in nanraka-no (build error). context_gate.py threshold 250k → 190k (user directive). **Session batch 70: 825 → 842 (+17 indexed).**

**BUILD common batch 71 DONE (2026-06-21, mixed common grab-bag — additive 'also/even' particles + concession/premise + respect/famous/state + worth/leverage/experience idioms + care/entrust + interval/every-time + means/both-and + emphatic topic):** 842 → **859 indexed** (+17), build PASS, lint clean (18), foreign-script scan clean. 1 redirect (te-wa-ikenai-kara→te-wa-ikenai). Additive: も又 (formal 'too' ↔ も) · にも (に+も stack, low→high; neg-sweep restriction). Concession/premise: とは言うものの (calm 'that said' ↔ とはいえ/ものの/のに) · を前提に (assumed condition ↔ を踏まえて). Respect/famous/state: 点で (single criterion ↔ において) · は〜で有名 (B takes で) · は〜となっている (formal established-state ↔ となる/ている). Worth/leverage/experience: 甲斐 (V-stem+がい rendaku) · を活かす (maximize-asset ↔ を使って) · 思いをする (emotion-adj, undergone). Care/entrust: に気をつける (に restriction ↔ に気がつく) · を〜に任せる (AをBに order). Interval/every-time: ぶり (**2-sense** interval-noun/manner-suffix, med→high ↔ ぶりに) · 度に (each-occasion ↔ ごとに/おきに). Means/both-and: ことにより/によって (formal nominalized-means ↔ ことで/によって) · も〜ば〜も (ば-frame ↔ も〜も/し). Emphatic topic: ったら (head topic w/ emotion ↔ って/は). **QA catches (×4):** stray 評価 kanji in English string (ten-de); typo `attaping_to:` dup key (ni-ki-o-tsukeru); duplicate `confidence:` key (buri, build error). **New gotcha folded into PASS §4:** seed already has `confidence:` — edit it, don't append a second. **Session batch 71: 842 → 859 (+17 indexed).**

**BUILD common batch 72 DONE (2026-06-21, deferred catalog-fold resolutions — drains the common band):** 859 → **860 indexed** (+1), build PASS, lint clean (4), scan clean. Resolved the long-pending fold decisions: o-suru → redirect → o-suru-2 (N4 already-enriched canonical お〜する); yaru → redirect → te-yaru (てやる benefactive owned by te-yaru); naze-nara-ba-kara-da → redirect → nazenara. **yaru-3 ENRICHED** as the standalone main verb やる = casual する 'to do/play' (low→high; no standalone する node; 花に水をやる 'give' note). **`common` band now DRAINED** — all remaining stubs are resolved noindex redirect-hubs. Next band = `--freq uncommon`. **Session batch 72: 859 → 860 (+1 indexed). Session total (b70–72): 825 → 860 (+35 indexed).**

**BUILD uncommon batch 73 DONE (2026-06-21, uncommon band opener — casual sentence-final question particles):** 860 → **862 indexed** (+2), build PASS, lint clean (2), scan clean. かい (warm yes/no question, softer than か; yes/no-only restriction, question-words take だい; ↔ だい/か) · かね (musing 'I wonder', か+ね; older/masculine ↔ かな/か). Tight self-contained pair opening the `uncommon` band. **Session batch 73: 860 → 862 (+2 indexed). Session total (b70–73): 825 → 862 (+37 indexed).**

**BUILD uncommon batch 74 DONE (2026-06-21, partial/quantity negation + だけ befitting/merit web + こと exclamatory + 'so to speak'/'for some reason' adverbs):** 862 → **880 indexed** (+18), build PASS, lint clean (18), foreign-script scan clean. **は-partial negation trio:** 全部は〜ない ('not all' — は makes it partial; bare = 'none') ↔ みんな〜ない ('not everyone'; bare みんな来ない can read 'no one') ↔ いつもは〜ない ('not always/usually'); めったに〜ない ('seldom', neg-locked ↔ あまり/全然); 〜ない〜はない (double-neg universal ≠ 〜ないことはない). **だけ web** (off dake, pivots さすが): だけあって ('as expected', positive ↔ だけに 'all the more', allows negatives ↔ からこそ) ↔ だけのことはある (verdict 'no wonder ~', さすが〜) ↔ だけのことはあって (て-form connective); だけましだ ('at least ~ is better' ↔ ましだ) ↔ だけ(のこと)だ ('simply a matter of ~' ↔ だけだ). **こと exclamatory:** ことか ('how very ~!') ↔ どんなに〜ことか (vs どんなに〜ても concessive trap) ↔ どれほど〜ことか. **'so to speak':** 言わば (written) ↔ 言ってみれば (spoken; ↔ つまり). **'for some reason':** どういうわけか (formal) ↔ どうしてだか (casual; vs どうして 'why?') — both ↔ なぜか. **Bumps:** metta-ni-nai low→high; zenbu-wa-nai/itsumo-wa-nai/dake-no-koto-wa-atte/donnani-koto-ka/dorehodo-koto-ka/dou-iu-wake-da-ka/doushite-da-ka/nai-wa-nai med→high; minna-wa-nai low→med. First real cluster-group of the uncommon band. **Session batch 74: 862 → 880 (+18 indexed). Session total (b70–74): 825 → 880 (+55 indexed).**

**BUILD uncommon batch 75 DONE (2026-06-21, temporal-span 'as long as/until end' + 'as for/instead of' connectives + か either-or/whether + degree/quantity は + N4 conditional/potential + futility):** 880 → **894 indexed** (+14), build PASS, lint clean (14), foreign-script scan clean. **Temporal span:** 〜間は (throughout vs 間に point-within) ↔ うちは ('as long as state lasts', ↔ うちに timing); 最後まで (emphatic まで); までで (cutoff/stopping-line, ↔ まで/までに). **Connectives:** に関しては (は-emphasis of に関して); に代わって ('instead of/on behalf of', formal ↔ 代わりに/の代わりに). **か:** か〜かどちらか (either-or, exactly-two ↔ か〜か/か〜ないか); かは〜によって違う ('whether ~ varies by', frame ↔ によって). **Degree/quantity は:** あまり(に)〜/あまりの〜に ('so ~ that' — あまり〜ない reductive vs あまりに〜 intensifying, same word opposite direction); 〔数量〕は ('at least', affirmative-floor vs 全部は〜ない negative-partial); 〜は〜くらいです (polite ballpark). **N4:** だら／だったら (casual copula conditional; だら colloquial variant; ↔ なら/たら); 聞ける (potential of 聞く 'can hear/ask' — vs 聞こえる involuntary-audible; ↔ れる/られる). **Futility:** 〜ても仕方がない ('no use ~ing' — THE trap vs てしかたがない 'can't help feeling'; ↔ 仕方がない/ても). **Bumps:** kikeru low→high, saigo-made/dara low→med, amari-2/aida-wa/made-de/ni-kanshite-wa/ka-ka-dochiraka/suuryou-wa/wa-kurai-desu med→high. **Session batch 75: 880 → 894 (+14 indexed). Session total (b70–75): 825 → 894 (+69 indexed).**

**BUILD uncommon batch 76 DONE (2026-06-21, ばかり aspect/connective web + 'even' emphatic):** 894 → **898 indexed** (+4), build PASS, lint clean (4), scan clean. ばかりだ (2-sense: ①one-way trend 'only keeps ~ing' ↔ 一方だ/ている; ②'all that's left is to ~'); ばかりか〜(さえ) ('not only ~ but even ~', literary escalation ↔ だけでなく/ばかりでなく/さえ); ばかりに ('simply because ~', single cause → bad result ↔ から/ので; せいで note); ですら ('even ~', literary/emphatic ↔ でさえ/すら/さえ). Tight batch near the context ceiling. **Session batch 76: 894 → 898 (+4 indexed). Session total (b70–76): 825 → 898 (+73 indexed).**

**BUILD uncommon batch 77 DONE (2026-06-21, self-contained N2 suffix/adverb):** 898 → **900 indexed** (+2), build PASS, lint clean (2), scan clean. 〜同士 ('among/between fellow ~, each other', reciprocal suffix; 似た者同士 set phrase); どこまでも ('endlessly/thoroughly/to the very end'). Both self-contained (no confusable sibling exists → contrasts correctly empty). Bumps: doushi/doko-made-mo med→high. **Milestone: 900 indexed.** Minimal batch at the context ceiling. **Session batch 77: 898 → 900 (+2 indexed). Session total (b70–77): 825 → 900 (+75 indexed).**

**BUILD uncommon batch 78 DONE (2026-06-21, こそあ-した demonstratives + definition/restatement frames + "no choice but to"/"nothing but" web + いられない modality):** 900 → **913 indexed** (+13), plus 2 conservative-noindex (low-conf) + 2 redirects; build PASS, lint clean (17), scan clean. **こそあ-した:** ああした (あ-series 'that kind, removed/known' ↔ ああいう) ↔ そうした (most common in writing ↔ そういう) — laddered vs kou-shita/kou-itta/sou-iu. **definition/restatement:** 前者は・後者は (former/latter, two-in-order, written); というのは事実だ (assert truth ↔ to-iu-no-wa/no-da); というのは〜ことだ (define a term ↔ tsumari/no-wa-no-koto-da); のは〜のことだ (LOW→conservative, noindex); ことなのだ (LOW→conservative, noindex). **"no choice but to":** よりほかない (canonical, med→high; ← yori-hoka-nai-2 redirect); よりしかたがない (しかた vs ほか swap); 以外にない (noun+verb, med→high); のほか(に)(は)〜ない (med→high; ← no-hoka-ni-nai redirect). **いられない trap trio:** ずにはいられない ('can't help DOING', する→せずに) ↔ ないではいられない (ないで-twin) ↔ てはいられない ('can't AFFORD to keep ~ing' — opposite stance) ↔ てばかりはいられない (ばかり over-indulgence). Folds yori-hoka-nai-2 & no-hoka-ni-nai stay noindex. Bumps: yori-hoka-nai/igai-ni-nai/no-hoka-ni-wa-nai/te-bakari-wa-irarenai med→high. Explore brief flagged sono-you-na & te-ageru as nonexistent → routed around. **Session batch 78: 900 → 913 (+13 indexed). Session total (b70–78): 825 → 913 (+88 indexed).**

**BUILD uncommon batch 79 DONE (2026-06-21, ない double-negative hedge + whether-or にしろ/にしても/なり set + "even if one wanted to, can't" potential-concession):** 913 → **924 indexed** (+11), plus 3 redirects; build PASS, lint clean (14), scan clean. **hedge:** ないこともない (canonical 'it's not impossible', nuance: understatement; ← nai-koto-mo-wa-nai redirect) ↔ なくもない (compact casual) ↔ ないでもない (feeling verbs) ↔ ないものでもない (formal); ないとも限らない ('can't rule out it won't', risk-warning ↔ とは限らない). **whether-or:** にしろ (canonical, now enriched) ↔ にしろ〜にしろ ↔ にしても〜にしても (softer) ↔ なり〜なり (choose-one, advice; ≠ literary なり). **potential-concession:** ようにも〜ない (volitional+にも+pot-neg same verb, external blocker; med→high; ← nimo-nai redirect) ↔ どうにも (adverb 'just can't', どうにもならない idiom; ← dou-ni-mo-nai redirect). Folds nai-koto-mo-wa-nai→nai-koto-mo-nai, nimo-nai→you-ni-mo-nai, dou-ni-mo-nai→dou-nimo stay noindex. **Session batch 79: 913 → 924 (+11 indexed). Session total (b70–79): 825 → 924 (+99 indexed).**

**BUILD uncommon batch 80 DONE (2026-06-21, まで "simply/merely a matter of" + "that's the end of it" modality):** 924 → **929 indexed** (+5); build PASS, lint clean (5), scan clean. **simply/merely:** までだ／までのことだ (canonical, のこと emphatic, covers V-る resolve + V-た merely-did ↔ dake-no-koto-da) ← るまでだ ('I'll simply ~', forward resolve) ↔ たまでだ ('I merely ~ed, nothing more', motive-deflection ↔ dake-da). **that's the end of it:** それまでだ (resigned finality/warning ↔ made-no-koto-da) ↔ ばそれまでだ (ば-condition 'if ~, it's all over'). Both まで sub-senses cross-linked. Tight batch near context ceiling. **Session batch 80: 924 → 929 (+5 indexed). Session total (b70–80): 825 → 929 (+104 indexed).**

**BUILD uncommon batch 81 DONE (2026-06-21, N1 standpoint pair + "forced to/compel" passive-causative pair):** 929 → **933 indexed** (+4); build PASS, lint clean (4), scan clean. **standpoint:** にしてみれば ('from ~'s point of view', てみる adds 'imagine being in their shoes' over plainer にしたら ↔ ni-shitara / ni-iwasereba / ni-totte) ↔ に言わせれば ('if you ask ~ / in ~'s opinion', voices the person's OPINION, 私に言わせれば = assert own view; causative 言わせる+ば, var に言わせると ↔ ni-shite-mireba felt-vs-spoken / ni-yoru-to neutral-source). **forced/compel** (formal/written, 余儀なく + する-noun): を余儀なくされる (PASSIVE 'be forced to', victim-subject, impersonal cause ↔ o-yoginaku-saseru mirror / zaru-o-enai verb-everyday / nakereba-naranai obligation-vs-loss-of-choice) ↔ を余儀なくさせる (CAUSATIVE 'compel into', cause-subject + person-に, rarer ↔ o-yoginaku-sareru mirror / saseru will-vs-circumstance). Mirror される victim-subject ↔ させる cause-subject made explicit; passive flagged as far more common. **Session batch 81: 929 → 933 (+4 indexed).**

**BUILD uncommon batch 82 DONE (2026-06-21, formal occasion / "prior to" / "after (much)" temporal connectives):** 933 → **940 indexed** (+7); build PASS, lint clean (9), scan clean. **occasion:** に際して (ceremonial 'on the occasion of', momentous undertaking + speech-act ↔ sai-ni / ni-atatte / toki) ↔ に当たって ('in undertaking', run-up + resolve; disambig from に当たる 'corresponds to') · 折 (polite/warm 'when', letters + seasonal greetings ↔ sai-ni / toki). **precedence:** に先立って／に先立ち ('prior to', preparatory step ↔ mae-ni / ni-sakigakete) ↔ に先駆けて ('ahead of OTHERS / be the first to', competitive pioneering ↔ ni-sakidachi). **after:** あげく(に) ('after much ~, ending BADLY', regrettable result, vs た末 neutral ↔ ta-sue / ato-de) · のち(に) (formal/literary 'after' ↔ ato-de). **Folds (stay noindex):** 末に (sue-ni) → ta-sue (に-form true dup) · 際 (sai) → sai-ni (bare noun → 際に construction). **Session b81–82: 929 → 940 (+11 indexed). Session total (b70–82): 825 → 940 (+115 indexed).**

**BUILD uncommon batch 83 DONE (2026-06-21, goal/aim/turning-point を-connectives + "unless/without there can be no" conditional-negatives):** 940 → **947 indexed** (+7); build PASS, lint clean (10), scan clean. **goal/aim:** を目指して ('aiming for', destination/end-point ↔ o-mokuhyou-ni) ↔ を目標に ('with the goal of', concrete benchmark + こと-clause ↔ o-mezashite). **turning-point:** を機に ('taking ~ as opportunity', shorter/everyday ↔ o-keiki-ni / ga-kikkake-de) ↔ を契機に ('as a turning point', formal/weighty ↔ o-ki-ni). **unless/without** (main clause negative): ないことには ('unless', indispensable precondition ↔ nakereba / te-hajimete) · なしでは ('without ~, … not', は-emphatic ↔ nashi-de / nashi-ni-wa) ↔ なしには (formal twin ↔ nashi-ni). **Folds (stay noindex):** をめぐって (o-megutte) → megutte-meguru · を中心に (o-chushin-ni) → o-chushin-to-ni-shite · ないことには〜ない (nai-koto-niwa-nai) → nai-koto-ni-wa. **Session b81–83: 929 → 947 (+18 indexed). Session total (b70–83): 825 → 947 (+122 indexed).**

**BUILD uncommon batch 84 DONE (2026-06-21, conviction / "only natural" modality):** 947 → **950 indexed** (+3); build PASS, lint clean (3), scan clean. にほかならない ('is nothing but / precisely', emphatic exact identification, 〜からにほかならない reason form ↔ ni-suginai opposite-valence / ni-chigainai guess-vs-assertion) · に相違ない ('no doubt that', formal/literary near-certainty ↔ ni-chigainai everyday-register / ni-hokanaranai) · のももっともだ ('only natural / no wonder', reaction justified by circumstances, empathetic ↔ touzen-da / atarimae-da). **Bump:** no-mo-mottomo-da med→high. **Milestone: 950 indexed. Session b81–84: 929 → 950 (+21 indexed). Session total (b70–84): 825 → 950 (+125 indexed).**

**BUILD uncommon batch 85 DONE (2026-06-21, rhetorical-denial modality pair):** 950 → **952 indexed** (+2); build PASS, lint clean (2), scan clean. ものか ('there's no way ~! / as if!', emotional defiant rhetorical rejection, question-shape = opposite meaning, もんか rougher ↔ wake-ga-nai calm-logical / hazu-ga-nai reasoned) · ことにはならない ('it doesn't mean that ~', denies a logical conclusion not a fact, often after からといって ↔ wake-de-wa-nai general-denial-vs-amounts-to). Lean batch at context ceiling. **Session b81–85: 929 → 952 (+23 indexed). Session total (b70–85): 825 → 952 (+127 indexed).**

**BUILD uncommon batch 86 DONE (2026-06-21, それどころか escalating contrast):** 952 → **953 indexed** (+1); build PASS, lint clean (1), scan clean. それどころか ('far from it / on the contrary / not only that', sentence-opener that denies the prior statement then escalates to a stronger opposite ↔ dokoroka within-sentence-attach vs standalone-opener / kaette ironic-reversal vs escalate-past-denial). Single lean node at context ceiling. **Session b81–86: 929 → 953 (+24 indexed). Session total (b70–86): 825 → 953 (+128 indexed).**

**BUILD uncommon batch 87 DONE (2026-06-21, instant-timing 'no sooner / on the verge' set):** 953 → **954 indexed** (+1 indexed + 2 redirects); build PASS, lint clean (3), scan clean. か〜ないかのうちに ('no sooner had ~ than'; same verb twice Vる+か+Vない+かのうちに, second event arrives before the first finishes — tighter & more literary than たとたん, past-fact second clause ↔ ta-totan / ya-ina-ya / ka-to-omou-to). Folds: かと思えば → redirect → ka-to-omou-to (ば-form variant); もう少し/ちょっとで〜するところ(だった) → redirect → tokoro-datta. Dedup-shaped batch — two near-dups folded rather than re-taught.

**BUILD uncommon batch 88 DONE (2026-06-21, 限{かぎ}り 'only / limit' family):** 954 → **956 indexed** (+2); build PASS, lint clean (2), scan clean. 〜限り/〜を限りに (the LIMIT 限り — reading-split from the enriched as-long-as conditional kagiri: N+限り 'only this once', N+を限りに 'as of ~/ending', 声を限りに 'to the utmost' ↔ kagiri / dake-da / kiri) ↔ に限って ('of all ~', singles one case out with ironic-bad-luck or trusting-denial attitude ↔ ni-kagiru 'nothing beats' / ni-kagirazu opposite-scope). Taught the 限 homograph grid: 限り(as-long-as) / 限り・を限りに(only) / に限って(of-all) / に限る(nothing-beats) / に限らず(not-limited-to). kagiri-2 conf med→high. no-hoka-ni-nai already a redirect → skipped.

**BUILD uncommon batch 89 DONE (2026-06-21, ところ-connective inference/situation set):** 956 → **959 indexed** (+3); build PASS (after a YAML fix), lint clean (3), scan clean. ところを見ると ('judging from' a scene the speaker watches → tentative guess, ends らしい/だろう ↔ koto-kara fact-grounds / tokoro-kara source-trace) · ところから ('from the fact that / which is why', circumstance as source a name/conclusion grew from ↔ koto-kara near-syn; disambig from ところ+から-3) · ところを ('at a moment when / caught in the act', ところ as object of next verb: polite お忙しいところを frame + caught-mid-action ↔ tokoro-ni event-arrives vs ところを verb-acts-on). tokoro-o conf med→high. **YAML trap:** inner double-quotes inside a double-quoted nuance string broke the build — strip nested `"` in prose (folded to PASS §gotchas).

**BUILD uncommon batch 90 DONE (2026-06-21, volitional よう/まい modality set):** 959 → **962 indexed** (+3); build PASS, lint clean (3), scan clean. ようではないか ('let's ~', oratorical 〜ましょう upgrade for speeches ↔ dewa-nai-ka plain 'isn't it?') · ようか〜まいか ('whether to ~ or not', speaker wavering over own action, feeds 迷う/悩む ↔ ka-dou-ka yes/no-fact / mai negative-volition half) · ようと/ようが ('no matter ~/whatever', emphatic concession off volitional+と/が, pairs question words, neg まいと/まいが ↔ you-tomo も-sibling / te-mo basic). you-to-ga conf med→high. Slug traps: かどうか = ka-dou-ka, ではないか = dewa-nai-ka.

**BUILD uncommon batch 91 DONE (2026-06-21, hearsay/quotation report set):** 962 → **964 indexed** (+2 indexed + 1 redirect); build PASS, lint clean (3), scan clean. との ('the ~ that', formal/written という that hangs reported content on a communication/thought noun 連絡/指示/見方 — news & business ↔ to-iu spoken-default) ↔ とのこと ('I'm told that ~', polite relayed hearsay for business messages, speaker = messenger not source ↔ souda plain-hearsay / to-iu-koto-da hearsay+conclusion). Fold: とかで → redirect → toka-2 (already covers the vague-reported-reason 急用ができたとかで). Watch double `formation:` keys (duplicated-mapping-key) — caught in to-no pre-build.

**BUILD uncommon batch 92 DONE (2026-06-21, 次第 'as soon as / depending on' pair):** 964 → **966 indexed** (+2); build PASS, lint clean (2), scan clean. 次第 (senses node: ①Vます+次第 'as soon as', formal future-only — can't describe a past event ②N+次第だ 'depends entirely on' 君の努力次第だ; +という次第だ note ↔ tara-sugu everyday past-or-future / ni-yoru neutral varies-by) ↔ 次第で ('depending on X the outcome varies', adverbial vs 次第だ predicate; 次第では branch-flag ↔ ni-yotte neutral). shidai conf med→high.

**BUILD uncommon batch 93 DONE (2026-06-21, て-form determination / extreme-means pair):** 966 → **968 indexed** (+2); build PASS, lint clean (2), scan clean. てでも ('even by ~/even if it means ~', extreme means + strong-will clause 借金してでも買いたい ↔ te-mo general concession / sae-ba minimum-condition opposite end) ↔ てみせる (senses: ①demonstrate to someone やってみせる ②resolve 'just watch' 必ず合格してみせる ↔ te-miru tentative-inward vs てみせる outward demonstrate/vow). te-miseru conf med→high.

**BUILD uncommon batch 94 DONE (2026-06-21, additive/escalating connective set):** 968 → **971 indexed** (+3); build PASS, lint clean (3), scan clean. さらには ('and even/moreover', escalating — は marks next item a step up, caps rising list ↔ sara-ni plain / sono-ue comparable-extra) · なお ('note that/in addition', supplementary proviso opener for notices, appends caveat not argument ↔ sore-ni casual-besides) · それも ('and that too/at that', amplifies the SAME item with striking detail それも新車を ↔ sore-ni separate-point widens vs それも sharpens). sore-mo conf med→high.

**BUILD uncommon batch 95 DONE (2026-06-21, と-based relation/comparison connectives):** 971 → **974 indexed** (+3); build PASS, lint clean (3), scan clean. と並んで ('alongside/on a par with', same level/class 富士山と並んで ↔ to-tomo-ni joint / to-onaji-kurai equal-degree) · と同じく ('the same as/likewise', adverbial modifying following clause 去年と同じく ↔ to-onaji-de で-copula predicate) · と逆に ('contrary to/opposite of', polar reverse 予想と逆に ↔ hanmen two-sides-of-same vs reverse-of-separate-ref / ni-taishite line-up-compare). と違って/反対に have no node — routed around.

**BUILD uncommon batch 96 DONE (2026-06-21, temporal moment/way set):** 974 → **976 indexed** (+2); build PASS, lint clean (2), scan clean. 瞬間（に） ('the moment that', V-た+瞬間 pinpoints single instant + coincident event; noun so refer-able その瞬間 ↔ ta-totan surprise-sequel vs neutral-pinpoint / ka-nai-ka-no-uchi-ni before-first-finishes; vs 一瞬 duration) · がけに ('on the way / just as ~ing', fixed motion-stem set 出/帰り/行き/通り/寝, non-productive ↔ tsuide-ni opportunity-of-main-task / nagara continuous-overlap). sai (際) already a redirect → skipped. **Session b87–96: 953 → 976 (+23 indexed + 5 redirects, 10 batches).**

**BUILD uncommon batch 97 DONE (2026-06-21, vague-listing particle set):** 976 → **978 indexed** (+2 indexed + 1 redirect); build PASS, lint clean (3), scan clean. やら (senses: ①question-word+やら 'something or other' 何やら ②clause+ことやら/のやら 'I wonder/who knows' どうなることやら ↔ ka indefinite neutral vs やら mystery) ↔ 〜やら〜やら ('what with X and Y', chaotic pile-up/mixed emotions 嬉しいやら悲しいやら, takes V/A ↔ ya neutral-noun-list / toka colourless). Fold: 〜や〜や → redirect → ya. yara/yara-yara conf med→high.

**BUILD uncommon batch 98 DONE (2026-06-21, それ-demonstrative connective pair):** 978 → **980 indexed** (+2); build PASS, lint clean (2), scan clean. それが ('actually/but against expectation', opener heralding a twist, esp. reply overturning question's assumption; disambig from それ+が subject-marking ↔ tokoro-ga written-however / sore-nanoni 'and yet') ↔ それは (senses: ①'as for that' topic pick-up ②emphatic 'that's really ~' それは大変でしたね, doubled それはそれは ↔ sore-ga twist / sore-ni adds-point). Both conf med→high. **Milestone: 980 indexed.**

**BUILD uncommon batch 99 DONE (2026-06-21, 〜ものと assumption/presumption modality family):** 980 → **985 indexed** (+5; dense N1 web); build PASS, lint clean (5), scan clean. ものと思う ('assume/take for granted' vs と思う opinion) ↔ ものと思っていた ('had assumed mistakenly', pairs てっきり) ↔ ものと思われる ('it is presumed', impersonal passive for reports ↔ to-kangaerareru) ↔ ものとする ('shall/stipulated', legal decree ↔ beki-da moral) ↔ ものとして ('on the assumption that', working premise ↔ to-shite real-role). The 〜ものと grid: 思う/思っていた/思われる/する/して. Slug traps: hazu-datta/to-omotte-ita/to-sareteiru have no node — routed around.

**BUILD uncommon batch 100 DONE (2026-06-21, 如何/いか- formal family):** 985 → **989 indexed** (+4; dense N1 web); build PASS, lint clean (4), scan clean. 如何（だ） ('nature/state of ~ an outcome hinges on', base for いかんで/いかんにかかわらず ↔ shidai) ↔ いかんで（は） ('depending on ~', formal 次第で; polarity flip いかんによらず='regardless' ↔ shidai-de / ni-kakawarazu) ↔ いかなる ('any/whatever ~', adnominal-before-noun formal どんな ↔ donna) ↔ いかに (senses: ①'how much ~' degree ②いかに〜ても concession ↔ dou / donna-ni-temo; いかにも separate idiom). The 如何 grid: 如何だ/いかんで/いかなる/いかに. ikan conf med→high. **Session b87–100: 953 → 989 (+36 indexed + 6 redirects, 14 batches).**

**BUILD uncommon batch 101 DONE (2026-06-21, formal scope/circumstance/concession connectives):** 989 → **997 indexed** (+8, grep 996) + 1 redirect; build PASS (after a `variants[].register` scalar→array fix), lint clean (9), scan clean. **topic/scope (に/は):** に関係なく ('regardless of', plainer twin of にかかわらず ↔ ni-kakawarazu / o-towazu category-opener; low→high) · にかけては ('when it comes to ~ [unbeatable]', main clause must be a confidence/superiority verdict — restriction ↔ ni-kakete the SPAN-use / ni-totte standpoint; low→high) · ついては (scoped to formal standalone connective 'and so/to that end', business; variant つきましては; ↔ ni-tsuite everyday について(は) which owns 'as for ~' — kept distinct to avoid dup; med→high). **formal circumstance (の):** の関係で ('owing to', vague circumstantial reason ↔ sei-de blame / tame-da explicit) · のもとで ('under [supervision/conditions]' ↔ ni-oite neutral-field; のもとに variant note). **concession:** とはいうものの ('that said', calm reasoned ↔ to-wa-ie compact-twin / mono-no clause-internal / noni emotional) · ことは〜が ('it's true that ~ but', repeated-word grudging concession; 〜には〜が note; **contrasts empty by design** — no confusable sibling; low→high) · まだしも ('~ would be one thing but', usually ならまだしも; nara-madashimo N1 same construction → future fold). **Fold:** の点で (no-ten-de) → noindex redirect → ten-de (点で formation already covers Nの点で). **New gotcha:** `variants[].register` is an array, not a scalar (folded to PASS §4).

**BUILD uncommon batch 102 DONE (2026-06-21, ものなら conditional pair + "if it is the case" conditionals + formal or/not-only listing):** 996 → **1003 indexed** (+7) + 2 redirects; **crosses 1,000 indexed**; build PASS, lint clean (9), scan clean. **ものなら pair** (potential-vs-volitional minimal pair): ものなら ('if one could ~', V-potential, wistful wish/dare ↔ you-mono-nara / nara) ↔ ようものなら ('if one were to ~, disaster', V-volitional, small action→outsized bad result; med→high). **conditionals:** のであれば ('if it is the case', formal のなら ↔ nara / ba) · ようでは ('if [such a poor state], then bad', consequence must be negative — restriction ↔ youda / te-wa; med→high) · たりしたら ('if for example ~', たり softens to one case/worry ↔ tara; たり has no node; med→high). **listing:** もしくは ('or', formal/written ↔ または / あるいは / か) · のみならず ('not only ~ but also', literary, のみ=formal だけ ↔ だけでなく / ばかりか). **Folds → mo-ba-mo (noindex):** も〜ば (front-half) · もし〜もする (する realization). **Session b101–102: 989 → 1003 (+14 indexed, grep).**

**BUILD uncommon batch 103 DONE (2026-06-21, worth/not-worth/no-need-to evaluative-modality web):** 1003 → **1010 indexed** (+7) + 1 redirect; build PASS, lint clean (8), scan clean. **worth:** 甲斐がある ('worth the effort', usually past 〜た甲斐があった ↔ kai-gai suffix / ni-atai-suru) · に値する ('worth/deserves', objective verdict ↔ ni-taranai opposite / ni-taeru) · に耐える (2-sense ①withstand ②be worth ~ing/hold up to scrutiny, neg 読むに耐えない; 〜の念に耐えない is a separate idiom; med→high). **not worth:** に足らない ('insignificant', formal 取るに足らない, 〜に足る positive ↔ ni-atai-suru / hodo-no-koto-wa-nai) · ほどのことはない ('no big deal', everyday, downplays the matter; absorbs では variant; low→high). **no need:** には及ばない (2-sense ①no need to ②be no match for ↔ niwa-ataranai) · には当たらない ('doesn't warrant [reaction]', reaction-verb-only restriction 驚く/褒める ↔ ni-wa-oyobanai). **Fold → hodo-no-koto-wa-nai (noindex):** ほどのことではない (は/では variant). ni-taru left a stub (noted 〜に足る in prose). **Session b101–103: 989 → 1010 (+21 indexed, grep).**

**BUILD uncommon batch 104 DONE (2026-06-22, N1 concessive space — universal "whether/no-matter" + "even so/nevertheless" connectives):** 1010 → **1019 indexed** (+9), no folds; build PASS, lint clean (9), scan clean. **Cluster A — universal concessive:** だろうが／だろうと (N/な-adj + conjecture, sweeps a question word/pair; restriction: verb → volitional 〜(よ)うが not 〜だろうが ↔ であれ / ようがまいが / ても) · であれ (formal/written, NOUN/疑問詞 only, individualizes each value; not on verbs ↔ だろうと colloquial-twin / ようとも / にかかわらず) · ようが〜まいが (V-vol + が + 同verb + まい + が, explicit do-or-don't; variant ようと〜まいと ↔ ようとも / だろうが / ても〜なくても) · ようとも (V-vol/かろう/であろう + とも, emphatic-literary, often どんなに〜 ↔ you-to-ga plainer / ようがまいが / ても). **Cluster B — "even so" connectives:** そうかといって (grants then BLOCKS over-conclusion, pairs わけにはいかない/わけではない, leans negative; variant かといって ↔ からといって reason-bound / それでも push-vs-pull / とはいえ) · それでいて ('and yet', two coexisting traits of SAME subject, after て-form; restriction: same-subject not two events ↔ のに / それでも) · しかしながら (formal/written しかし, no restriction by design ↔ しかし register-pair / とはいえ) · もっとも-2 (connective 'though/mind you', partial reservation trails 〜が; homograph note ≠ 最も / もっともだ ↔ しかし / ただし) · だろうに (modality; regret/reproach that counterfactual expectation didn't come true, after ば/たら ↔ のに / だろう). Anchored to enriched darou/de-aru/volitional-form/you-to-ga/shikashi/te-mo/noni/sore-demo/ni-kakawarazu/kara-to-itte/sore-de/datte (+ stub-but-exists to-wa-ie/tadashi/shikashi-nagara). **Session b101–104: 989 → 1019 (+30 indexed, grep).**

**BUILD uncommon batch 105 DONE (2026-06-22, N1 "tend to/apt to" + "as soon as/no sooner" temporal):** 1019 → **1026 indexed** (+7), no folds; build PASS, lint clean (7), scan clean. **Cluster A — tend to/apt to:** ともすれば (adverb, latent negative tendency, pairs 〜がち/〜やすい/〜かねない; restriction: general not one-time ↔ ともすると / がち) · ともすると (ば-twin, interchangeable ↔ ともすれば / どうかすると / がち) · きらいがある (V-る/Nの predicate 'regrettable tendency', negative-eval-only restriction ↔ がち / ともすれば / やすい) · どうかすると ('sometimes / under certain conditions', pairs こともある/かもしれない; **conf med→high** ↔ ともすると tendency-vs-occasional / かもしれない). **Cluster B — as soon as/no sooner:** が早いか (literary 'no sooner than', stresses speed, main-clause past sudden action — restriction ↔ や否や / なり / たとたん) · そばから (repeated futile cycle 'as fast as ~ undoes', restriction: repetition ↔ が早いか single-vs-recurring / たとたん) · た弾みに ('with the momentum of', physical-accidental result; variant 弾みで ↔ たとたん). Anchored to enriched gachi/yasui/kamoshirenai/ta-totan/nari/ya-ina-ya. **Session b101–105: 989 → 1026 (+37 indexed, grep).**

**BUILD uncommon batch 106 DONE (2026-06-22, N1 three tight pairs: covered-in/full-of + each/respectively + listing-examples):** 1026 → **1031 indexed** (+5); build PASS, lint clean (5), scan clean. **covered-in triangle:** まみれ (N + 'coated in dirty substance' 泥/血/汗, always negative; restriction: clinging substance ↔ だらけ scattered-countable / ずくめ composed-of) · ずくめ (N + 'entirely/nothing but', fixed set 黒/いいこと/規則, **neutral-to-positive** unlike まみれ/だらけ ↔ だらけ / まみれ). **each/respectively:** 銘々 (each person, formal-literary, people-not-things restriction ↔ それぞれ / 各々) · 各々 (formal-written, slightly broader, **conf low→high** ↔ 銘々 / それぞれ). **listing-examples:** だの〜だの (grumbled examples w/ dismissive tone, takes N/adj/V/quotes, negative-attitude restriction ↔ や neutral / とか / なり〜なり choose-alternatives; **conf med→high**). ya-ya left as existing noindex redirect→ya (thin by design). Anchored to enriched darake/sorezore/ya/toka/nari-nari. **Session b101–106: 989 → 1031 (+42 indexed, grep).**

**BUILD uncommon batch 107 DONE (2026-06-22, N1 に-particle standard/basis cluster + にまつわる):** 1031 → **1035 indexed** (+4); build PASS, lint clean (4), scan clean. **"in accordance with/based on/in light of" web** (off enriched ni-motozuite/ni-shitagatte/ni-sotte): に即して (adapt to *concrete reality* 実情/現実, restriction: facts not abstract rule ↔ ni-nottotte / ni-terashite / ni-motozuite) · に照らして (evaluate *against a standard/law* 法律/経験/常識, yardstick restriction ↔ ni-nottotte conform-vs-evaluate / ni-sokushite) · に則って (*conform strictly to* rule/custom/ceremony 規則/伝統, restriction ↔ ni-shitagatte broad-vs-formal / ni-sokushite / ni-terashite) — the 則/即/照 three-way is the GEO win. **にまつわる** (adnominal-only 'tales/associations entangled around', restriction: no adverbial *にまつわって話す ↔ ni-kanshite / ni-tsuite / o-megutte contested-vs-no-conflict). を中心に (→o-chushin-to-ni-shite) and をめぐって (→megutte-meguru) left as pre-shaped noindex redirects. **QA:** a Cyrillic phrase (связанные с) slipped into an English example mid-write — caught & fixed before scan. Anchored to enriched ni-motozuite/ni-shitagatte/ni-sotte/ni-kanshite/ni-tsuite/o-megutte. **Session b101–107: 989 → 1035 (+46 indexed, grep).**

**BUILD uncommon batch 108 DONE (2026-06-22, N1 "let alone/all the more/much more" escalation cluster):** 1035 → **1039 indexed** (+4); build PASS, lint clean (4), scan clean. The a-fortiori web: まして(や) (sentence-connective bridging two clauses, escalates from a baseline; restriction: needs preceding statement ↔ はおろか / なおさら / どころか same-direction-vs-contradiction) · はおろか ('not even B, let alone A' both denied in ONE clause, 2nd noun も/さえ/すら + neg; negative-clause restriction; **conf low→high** ↔ ましてや two-clause / どころか can-flip-positive) · なおさら (degree adverb 'all the more' given an added reason, often consequent of ましてや ↔ さらに add-on-vs-intensify / にも増して) · にも増して (N + 'more than [already-high benchmark]', set phrase 何にも増して ↔ より everyday-vs-formal / なおさら). Anchored to enriched dokoroka/sara-ni/yori. **Session b101–108: 989 → 1039 (+50 indexed, grep).**

**BUILD uncommon batch 109 DONE (2026-06-22, N1 "as if to say/almost about to" ばかり-modality cluster):** 1039 → **1042 indexed** (+3); build PASS, lint clean (3), scan clean. とばかりに (quote + 'as if to say', message via manner not voiced; observable-action restriction ↔ to-iwan-bakari-ni / n-bakari-ni) · と言わんばかりに (the 言う-instance of んばかり, 'all but saying', 言わん = classical neg-volitional ↔ to-bakari-ni shorter / n-bakari-ni) · んばかり(に) (V-ない-stem + 'almost on the verge of ~ing' hyperbole, action does NOT occur, **する→せんばかり** ↔ to-iwan-bakari-ni same-root / kakeru nearly-vs-actually-begun). Split: manner-message vs near-action hyperbole, と言わんばかりに the bridge. Anchored to enriched bakari/bakari-ni/bakari-da/kakeru. **Session b101–109: 989 → 1042 (+53 indexed, grep).**

**BUILD uncommon batch 110 DONE (2026-06-22, five formal-written clusters):** 1042 → **1063 indexed** (+21); build PASS, lint clean (21), scan clean. **Cluster A — formal additive/restatement connectives:** かつ (within-clause 'and also', stacks parallel attributes ↔ 及び/並びに/そして) · 並びに (formal noun-list 'and'; 及び-vs-並びに legal hierarchy ↔ to-2/かつ) · ないし(は) (senses: 'or' formal + 'from~to~' range ↔ mata-wa/aruiwa) · すなわち ('namely', precise equivalent 'i.e.' ↔ tsumari/yousuru-ni) · 加えて ('in addition', opener; に加えて noun-bound note ↔ sono-ue/さらに) · それゆえ ('therefore', literary ↔ yue-ni/だから/それで). **Cluster B — 至る reach/extent:** に至る (culminate in grave endpoint; に至っては/geographic notes ↔ ta-sue/に至るまで) ↔ に至るまで ('down to even', full reach ↔ made/kara-ni-itaru-made) ↔ から〜に至るまで ('from A all the way to B' ↔ kara-made). **Cluster C — を-connectives:** を経て (via/pass-through ↔ を通して/てから) · を介して (through-intermediary ↔ を通じて/を通して) · を兼ねて (serving-also-as ↔ がてら/かたがた/ついでに) · を皮切りに (starting-with → expanding series ↔ を経て/kara-3) · をもって (senses: by-means-of formal + as-of boundary-time ↔ によって/で) · をいいことに (exploit unfairly, disapproving ↔ を機に). **Cluster D — while-also/dual-purpose:** がてら (casual motion-leaning ↔ ついでに/を兼ねて/ながら) · かたがた (formal courteous, letters ↔ がてら/を兼ねて/ついでに) · ながらに (literary 'while remaining', fixed 涙/生まれ/昔ながら ↔ nagara/mama). **Cluster E — 'it's not as if' + label-denial:** ではあるまいし (rejects exaggerated premise → rebuke ↔ じゃあるまいし/わけではない/まるで〜ようだ) ↔ じゃあるまいし (casual twin) · でも何でもない ('not ~ in the least', denies label ↔ 全然〜ない/わけではない/まったく〜ない). No folds. **Session batch 110: 1042 → 1063 (+21 indexed, grep 1063).**

**BUILD uncommon batch 111 DONE (2026-06-22, degree adverbs + 済む modality + と "when it comes to"):** 1063 → **1082 indexed** (+19); build PASS, lint clean (19), scan clean. **Cluster 1 — formal degree/extent adverbs:** 極めて (formal extremely ↔ totemo/かなり) · さぞ (empathetic 'I can imagine', pairs でしょう ↔ きっと/だろう) · 概ね (on the whole, med→high ↔ だいたい/およそ) · およそ (senses: roughly + utterly+neg ↔ だいたい/概ね) · 辛うじて (barely, slim margin ↔ やっと) · まるっきり (casual completely+neg ↔ まるで/全然/まったく) · ことごとく (every single one, literary, contrasts empty §6-B) · たかが (merely, belittles ↔ たった/だけ/に過ぎない) · 強いて (if pressed, 強いて言えば ↔ あえて). **Cluster 2 — 済む resolution-modality:** 済む (senses: be-finished/be-settled, med→high ↔ 終わる/ずに済む) · 済ませる (transitive, low→high ↔ 済む/終わる) · では済まない (won't end with just ↔ ずにはすまない/て済むことではない/どころではない) ↔ ずにはすまない (can't get away without, social/moral, する→せずに ↔ ざるを得ない/なければならない/ずに済む) · て済むことではない (alone won't settle it ↔ では済まない/て済む). **Cluster 3 — と "when it comes to / given that":** ときたら (exasperated complaint-topic ↔ となると/ともなると/は) · ともなると／となると (notable level, med→high ↔ となると/になると/ときたら) · とあって (because, newsworthy circumstance, reportive ↔ から/ので/とあっては) ↔ とあっては (if such is the case→obligation ↔ とあって/とあれば/なら) ↔ とあれば (if it's for ~, willing readiness ↔ とあっては/なら/たら). No folds. **Session b110–111: 1042 → 1082 (+40 indexed, grep 1082).**

**BUILD uncommon batch 112 DONE (2026-06-22, ならでは + 'if X own-issue' pair + に contrast/non-limit + predicament modality):** 1082 → **1093 indexed** (+11, +2 noindex folds); build PASS, lint clean (13), scan clean. **A — ならでは:** ならでは (distinctive of, praising, ならではの+N ↔ だけあって/こそ) ← ならではの → redirect → nara-dewa · ならまだしも → redirect → madashimo (b101 fold resolved). **B — 'if X, own side' pair:** なら〜で (N/な-adj, resigned ↔ tara-tade/なら) ↔ たら〜たで (V/adj-past, あればあったで variant ↔ nara-de/たら). **C — に contrast/non-limit:** にひきかえ (subjective contrast of two different things, med→high ↔ に対して/反面/に比べて) · に留まらず (spreads beyond, formal ↔ だけでなく/ばかりか/に限らず) · によらず (regardless of, literary, 見かけによらず ↔ にかかわらず/を問わず/にもかかわらず). **D — predicament/no-end modality:** 羽目になる (end up stuck ↔ ことになる/始末だ) · 始末だ (sorry end-state, critical ↔ 羽目になる/あげく) · 切りがない (no end to; contrasts empty §6-B) · 術がない (no means, literary ↔ 仕方がない/よりほかない) · ないものか (wistful 'isn't there a way?'; homograph note vs defiant ものか ↔ てほしい/だろうか). Folds (noindex, sai.md-style): nara-de-wa-no, nara-madashimo. **Session b110–112: 1042 → 1093 (+51 indexed, grep 1093).**

**BUILD uncommon batch 113 DONE (2026-06-22, ても disclaimer/futility/intensity + 'it's about/practically' estimation):** 1093 → **1101 indexed** (+8); build PASS, lint clean (8), scan clean. **A — ても disclaimer/futility/intensity:** て敵わない (unbearably, neg-only, disambig かなわない 'no match' ↔ てたまらない/てしかたがない) · てもどうにもならない (action futile, situation fixed ↔ どうにも/仕方がない/ても) · ても知らない (don't-blame-me warning, casual, med→high ↔ ても/と) · ても差し支えない (formal permission 'no hindrance' ↔ てもいい/てもかまわない). **B — 'it's about/practically' estimation:** といったところだ (about/at most, pairs せいぜい ↔ というところだ/ぐらい) ↔ というところだ (near-syn, disambig literal 'the point where' ↔ といったところだ/ぐらい) · くらいのものだ (about the only one, dismissive ↔ だけ/しかない/ぐらい) · も同然だ (practically/as good as, 〜ようなものだ near-equiv ↔ と同じくらい/ぐらい). No folds. **Session b110–113: 1042 → 1101 (+59 indexed, grep 1101).**

**BUILD uncommon batch 114 DONE (2026-06-22, five clusters: without/missed-chance + counterfactual/pretense + limit/unreasonable/never-happened + expressive estimation + temporal ever-since):** 1101 → **1127 indexed** (+26); build PASS, lint clean (26), scan clean. **A — without / failed to / missed chance:** ことなしに (written 'without ~ing', X-as-necessary-means ↔ koto-naku/zu-ni/nashi-ni) · もしないで (emphatic 'without even ~ing', reproach ↔ nai-de/zu-ni) · ないでも (concessive 'even without ~ing' ↔ nakute-mo/nai-de) · ともなく (senses: aimless-action 見るともなく + vague-source どこからともなく ↔ to-mo-nashi-ni) ↔ ともなしに (literary twin, aimless-only ↔ to-mo-naku; med→high) · ずじまい (ended up never ~ing, regret, する→せず ↔ sobireru/zu-ni) · そびれる (miss the timing/chance, hesitation ↔ sokonau/zu-jimai) · 損{そこ}なう (senses: fail-to-do + do-wrongly; 死に損なう 'narrowly' note; 損ねる variant ↔ sobireru). **B — counterfactual/pretense:** たら〜ところだ (counterfactual narrow-miss 'would have, but didn't', pairs 危うく ↔ tokoro-datta/sou-ni-naru) · たところで (concessive futility 'even if ~, useless', neg main clause, た≠past ↔ te-mo/ta-tokoro; ところで 'by the way' note) · たことにする (pretend ~ (didn't) happen, chosen fiction; med→high ↔ furi-o-suru/koto-ni-suru/ka-no-you-da) · たつもりはない (deny intent/deed 'didn't mean to' ↔ tsumori-datta/tsumori) · たくても〜ない (thwarted desire 'can't even if want to', same-verb potential-neg; med→high ↔ you-ni-mo-nai/te-mo). **C — limit/unreasonable/never:** にもほどがある (indignant rebuke 'there's a limit to', nuance fires ↔ sugiru) · には無理がある (points out a flaw/stretch; vs 無理だ 'impossible' note) · ためしがない (never-once track-record, critical; vs ことがない note) · 限{かぎ}りだ (peak emotion 'couldn't be more ~', emotion-adj only ↔ kagiri homograph/to-ittara-nai) · 心配がある (personal worry/risk; med→high ↔ osore-ga-aru forecast/kanousei-ga-aru neutral). **D — expressive estimation:** といおうか (groping for the word 'or should I say', often doubled ↔ to-iu-yori/mushiro) · と言えなくもない (cautious double-neg 'one could even say', hedges a judgment ↔ to-ieru/nai-koto-mo-nai) · といったらない (indescribably ~, colloquial peak degree; ありゃしない/ったらない variants ↔ kagiri-da; vs といったところだ note) · とは比べものにならない (different league, comparison meaningless ↔ yori/to-onaji-kurai antonym) · たとえて言えば (announce an analogy, pairs ようだ ↔ iwaba direct-label). **E — temporal:** てからというもの (emphatic 'ever since', lasting change ↔ te-kara/irai) · たら最後 (irreversible bad result 'once you ~, no going back'; たが最後 variant ↔ tara) · たなり (literary 'left just as ~, nothing more', neglect ↔ mama/kiri; vs as-soon-as なり note; med→high). **Confidence bumps:** to-mo-nashi-ni/ta-koto-ni-suru/takute-mo-nai/shinpai-ga-aru/ta-nari-de med→high. **Seed-title fix:** tara-saigo (unclosed paren). No folds, no QA slips. **Session batch 114: 1101 → 1127 (+26 indexed, grep 1127).**

**BUILD uncommon batch 115 DONE (2026-06-22, three clusters: quality-acquisition suffixes + emphatic negation adverbs + expectation/impulse/retrospection adverbs):** 1127 → **1141 indexed** (+14, +1 redirect); build PASS, lint clean (15), scan clean. **A — quality-acquisition suffixes (4):** 〜びる (Noun+びる ichidan, natural/gradual quality often via age/wear 古{ふる}びる/大人{おとな}びる, involuntary ↔ buru deliberate-pose/meku touch-of/ppoi everyday-ish) · 〜ぶる (Noun/な-adj+ぶる godan, deliberate phony pose 偉{えら}ぶる/知{し}ったかぶる, critical; restriction: implies pretense ↔ biru natural-acquire/furi-o-suru one-off-pretend/garu shows-real-feeling) · 〜めく (Noun+めく godan, 'show signs of/touch of' 春{はる}めく/謎{なぞ}めく, literary, adnominal めいた ↔ biru fully-acquire/jimita negative-vs-atmospheric) · 〜じみた (Noun+じみた, negative 'unbecomingly tinged with' 子供{こども}じみた/所帯{しょたい}じみた; restriction: negative-only ↔ ppoi neutral/meku atmospheric/buru deliberate-pose; from 染{じ}みる). **B — emphatic negation adverbs (4 indexed + 1 redirect):** 何ら〜ない (formal categorical 'not any whatsoever', abstract nouns; med→high; 何らの variant ↔ mattaku everyday/sukoshi-mo degree) · とうてい〜ない (到底, 'cannot possibly, no effort suffices'; med→high; neg-bound restriction ↔ totemo〜ない near-syn-everyday/zenzen degree-zero) · あながち〜ない ('not necessarily/entirely', concedes partial truth, fixed neg endings ↔ to-wa-kagiranai predicate-vs-adverb; 必ずしも prose) · 〜として〜ない (一+counter+として+neg 'not even one' 一日{いちにち}として; med→high; restriction: 一 fixed ↔ sukoshi-mo degree/nanra-nai abstract-vs-counted) ← **一〜として〜ない (ichi-to-shite-nai) → noindex redirect → to-shite-nai** (same construction, 一 obligatory). **C — expectation/impulse/retrospection adverbs (6):** 案の定 ('sure enough, as feared', predicted bad outcome confirmed ↔ yahari neutral-good-or-bad/hatashite formal+question-use) · 果たして (**senses**: ①'sure enough' confirm prediction ②'(really?)' opens doubtful question 〜だろうか ↔ an-no-jo feared-only/yahari everyday) · 思わず ('involuntarily/reflexively', reflex to stimulus, +てしまう; restriction: unintended ↔ tsui lapse-against-judgment/ukkari careless-mistake) · 思い切って ('boldly/take the plunge', overcome own hesitation ↔ aete dare-hard-option-on-purpose/omowazu deliberate-vs-reflex) · 思えば ('looking back/now that I think of it', retrospective opener 今思えば; med→high; ba-conditional of 思う, no confusable sibling → contrasts empty §6-B) · 見るからに ('visibly/obviously at a glance', from appearance, +そうな; restriction: visible-only ↔ ikanimo fits-stereotype/akiraka-ni any-evidence-incl-reasoning). **Confidence bumps:** nanra-nai/toutei-nai/to-shite-nai/omoeba/ichi-to-shite-nai med-or-low→high. **Missing-target notes (→ prose):** 必ずしも (kanarazushimo-nai)/hitotsu-mo-nai/kangaete-mireba absent — routed to prose. No QA slips. **Session batch 115: 1127 → 1141 (+14 indexed, grep 1141).**

**BUILD uncommon batch 116 DONE (2026-06-22, four clusters: enumeration openers + hypothesis/whether + formal occasion + そこを/にして particles):** 1141 → **1150 indexed** (+9, +1 redirect); build PASS, lint clean (10), scan clean. **A — enumeration / 'for one thing / on one hand' (4):** 第一{だいいち} ('first of all / for one thing', foregrounds the foremost point, also 'above all'; med→high ↔ hitotsu-ni-wa one-of-several) · 一つ (**senses** ①'for one thing' point-marker ②softener '(just/kindly) ~' ひとつよろしく/やってみよう; low→med, review_reason ↔ hitotsu-ni-wa crystallized-connective) · 一つには ('for one thing, one reason being', explicit enumeration pairs 二つには; med→high ↔ daiichi ranking/hitotsu softener-sense) · 一方では〜他方では〜 (balances two coexisting sides, formal; med→high ↔ ippou-de single-add / hanmen same-thing-two-sides). **B — hypothesis / whether (2):** 仮に ('supposing/hypothetically', flags premise as not-real, pairs 〜としたら/〜としても ↔ moshi-mo real-if / tatoe-temo concessive) · 〜か否か (formal/written 'whether or not', 否=classical no ↔ ka-dou-ka everyday-spoken / ka-ka two-named-alternatives). **C — formal occasion (1 indexed + 1 redirect):** 節に ('on the occasion of', polite correspondence set-phrase その節は; med→high ↔ ori warm-general / sai-ni neutral-official) ← **折には (ori-niwa) → noindex redirect → ori** (は-marked form, ori already covers 折に/折には). **D — particles (2):** そこを ('despite that / I-know-but', plea to override a stated obstacle, そこを何とか/曲げて; med→high ↔ noni neutral-although) · 〜にして (**senses** ①'at/even at a stage/age' 六十にして/この年にして初めて ②'in an instant' 一瞬にして/一夜にして ↔ sae extreme-example-vs-point-on-scale; 今にして思えば note). **o-4 (emotive を) deferred** — ものを already enriched as mono-o; bare emotive を obscure/low-conf, left for a rare-particle pass. No QA slips. **Session b115–116: 1127 → 1150 (+23 indexed, grep 1150).**

**BUILD uncommon batch 117 DONE (2026-06-22, three adverbial clusters: evaluative/manner + temporal-stance + emotion/reference/degree):** 1150 → **1164 indexed** (+14); build PASS, lint clean (14), scan clean. **A — evaluative/manner adverbs (5):** いかにも ('every bit the ~ / just like a typical ~' + intensifier 'truly', pairs 〜らしい/〜そう; standalone 'indeed' agreement note ↔ miru-kara-ni visible-at-a-glance-vs-fits-stereotype) · あくまでも (**senses** ①persist-to-the-end ②strictly/merely-qualify 個人的意見にすぎない; variant あくまで ↔ doko-made-mo limitless-extent-vs-unwavering-stance) · 中途半端 (な/に 'halfway/half-hearted', almost-always-negative; med→high; no confusable sibling → contrasts empty §6-B) · 下手に ('rashly/ill-advisedly → backfires', pairs と/ば+bad-result; restriction: not the plain adverb of 下手 skill; med→high; contrasts empty) · それなりに ('in its own way/reasonably', fixed pronoun-phrase ↔ nari-ni noun-attached-whose-own-way; それなりの+N note). **B — temporal-stance adverbs (3):** 今更 ('now of all times / too late', pairs ても/neg/rhetorical-Q; restriction: not neutral 'now'; 今更ながら set-phrase) · 一旦 (**senses** ①'once ~ → inevitable consequence' +たら/と ②'for the time being' 中断; 一度 count-vs-turning-point note) · 依然(として) ('still/as before, unchanged', formal/written ↔ speech 相変わらず/まだ; variant 依然 drops として). **C — emotion/reference/degree (6):** ことに ('to one's surprise/joy/regret', emotion-word-fronted; restriction: emotion/eval words only ×高いことに; prereq koto) · 割合 ('comparatively/fairly', plain adverb; med→high; variant 割合に ↔ wari-ni-wa against-a-stated-yardstick; prereq wari-ni-wa; vs noun 割合 'ratio') · ただの ('a mere/just a ~', NOUN-attach restriction vs adverb ただ ↔ tada adverb-merely / dake quantity-vs-quality-downplay) · 例の ('that ~ we both know', shared-knowledge/discreet; 例のごとく 'as usual' note) · そのもの ('the very ~ / embodiment of', N/な-adj-stem; med→high ↔ jitai singles-out-to-evaluate-vs-intensify-embodiment) · 僅か ('only/a mere/slight', number/amount/degree; med→high ↔ wazuka-ni adverb-slightly / tatta number-only-vs-broader-formal). Anchored to enriched miru-kara-ni/doko-made-mo/nari-ni/koto/wari-ni-wa/tada/dake/jitai/wazuka-ni/tatta. **Confidence bumps:** chuto-hanpa/hetani/wariai/sono-mono/wazuka med→high. **Fix caught mid-write:** dropped a mismatched ittan↔ichido-ni contrast (一度に = 'all at once', not 一度 'one time') → moved to a note. No QA slips. **Session batch 117: 1150 → 1164 (+14 indexed, grep 1164).**

**BUILD uncommon batch 118 DONE (2026-06-22, five clusters: こと-reason connectives + parity/extent suffixes + listing/aside connectives + dependency/concession conditionals + effort-in-vain):** 1164 → **1178 indexed** (+14); build PASS, lint clean (14), scan clean. **A — こと-connectives (3):** ことだし ('since ~ among other things', soft justification → decision/suggestion ↔ koto-dakara predict-from-character / shi plain-reason-stack) · こともあって ('partly because ~', one factor behind an already-arisen result ↔ koto-dashi leads-to-decision / sei-de pins-one-bad-cause) · ことのないように (emphatic negative purpose 'so that ~ never happens' ↔ youni general-purpose / koto-naku without-doing). **B — parity/extent suffixes (3):** 並み ('on a par with / up to ~ level', compact N-suffix ↔ to-onaji-kurai roughly-equal-degree; 人並み/軒並み note) · ぐるみ ('the whole ~ together / ~-wide', group-noun-only restriction 家族/会社/町; collective-wrongdoing note; contrasts empty §6-B) · 来{らい} ('for the past ~', span-suffix continuing-to-now; low→high ↔ irai ever-since-an-event-vs-duration-suffix; 本来/従来/将来 fixed-vocab note). **C — listing/aside connectives (3):** といい〜といい ('what with A and B alike', two facets → one evaluation; med→high ↔ mo-mo plain-add / ni-shiro-ni-shiro concessive-choice-vs-supporting-evidence) · と相まって ('coupled with ~', two factors interact→amplify, formal ↔ ni-kuwaete merely-adds / to-tomo-ni together-with) · はさておき ('setting ~ aside → to the main point'; med→high ↔ wa-tomokaku conversational-dismissive / wa-betsu-to-shite neutral-deferral). **D — dependency/concession (3):** あっての ('the A that only B makes possible', N1あってのN2 ↔ nakushite-wa negative-condition-clause / nashi-ni-wa without-before-verb; 命あっての物種 proverb) · なくして(は) ('without ~, there can be no ~', formal, negative/impossible main clause ↔ nashi-ni-wa everyday / nai-koto-ni-wa verb-clause-unless) · ないまでも ('even if not ~, at least ~', concedes bigger-action-won't-happen + asserts lesser, set frame 〜とは言わないまでも ↔ nakute-mo even-without). **E — effort-in-vain (1):** 甲斐もなく ('despite ~, to no avail', disappointing outcome ↔ kai-ga-aru paid-off-opposite / kai-gai 〜がい worthwhile-suffix). **Confidence bumps:** rai low→high; to-ii-to-ii/wa-sate-oki med→high. No QA slips. **Session b117–118: 1150 → 1178 (+28 indexed).**

**BUILD uncommon batch 119 DONE (2026-06-22, four clusters: surprise-contrast & scope-denial + number/composition particles + sentence-final particles/registers + condition/dual-nature/warning):** 1178 → **1192 indexed** (+14); build PASS, lint clean (14), scan clean. **A — surprise/scope-denial (4):** かと思いきや ('just when one thought ~, contrary to expectation', literary ↔ ka-to-omou-to quick-succession-vs-contradicted-expectation) · 全ては〜ない ('not all', は-partial-negation; med→high; restriction: は essential else total denial ↔ zenbu-wa-nai everyday-twin) · に限ったことではない (sentence-final 'not limited to just ~' ↔ ni-kagirazu mid-sentence-opener / ni-kagitte singles-out opposite-job) · どころの話ではない ('far from it / out of the question'; med→high ↔ dokoro-de-wa-nai base / dokoroka reverses-to-opposite). **B — number/composition (3):** からある ('as much/many as / no less than', からする prices/からいる people ↔ mo-2 everyday-number-も) · からなる ('consist of / composed of', structured whole ↔ de-dekiru physical-material-vs-constituent-parts) · 単位で ('by units of / per ~'; med→high ↔ goto-ni each-vs-unit-of-measure). **C — sentence-final particles/registers (4):** たまえ (man's gentle command to inferior, dated, Vます-stem ↔ nasai gender-neutral / imperative blunt) · とも ('of course/certainly' emphatic affirmative; med→high ↔ yo informs-vs-confirms; disambig concessive/quotative とも) · わ (soft feminine emphasis; title-fix truncated→full ↔ yo asserts-outward / ne seeks-agreement) · ときに ('by the way', formal/dated topic-break; med→high ↔ tokoro-de everyday / sate own-agenda-next; disambig 〜ときに 'when'). **D — condition/dual-nature/warning (3):** ようによっては ('depending on how/the manner', V-stem+よう+によっては ↔ you base-way / shidai-de factor-vs-manner) · でもあり〜でもある ('is both A and B at once', coexisting/paradoxical identities ↔ de-mo-aru single-also / mo-mo lists-vs-assigns-identities) · さもないと ('otherwise / or else', standalone warning ↔ de-nai-to condition-bound / nakereba neutral-conditional). **Confidence bumps:** subete-wa-nai/dokoro-no-hanashi-de-wa-nai/tani-de/tomo/toki-ni med→high. **Seed-title fix:** wa-3. No QA slips. **Session b117–119: 1150 → 1192 (+42 indexed).**

**BUILD step 1 DONE (2026-06-05):** the 8 form-anchors (SLICE Finding 2) are promoted to
real catalog rows (`grammar_enriched.csv` = 1,527, `family=form`) + real teaching pages in
a bootstrapped Astro Content Collection (`src/content.config.ts` + 8 `.md` files); all
`*<anchor>` prereqs flipped to bare slugs; `build_slice.py` resolves anchors from the
catalog; QA + `npm run build` PASS.
**BUILD step 2 DONE (2026-06-11):** same-surface dedup/sense review (SLICE Finding 3).
All **78 same-surface clusters (175 nodes)** in the full catalog adjudicated by hand —
keep-distinct (genuine sense, #3) vs merge (OCR/cross-row dup). **69 dups merged →
`grammar_enriched.csv` = 1,458**; sense-splits kept (を×4, に×5, られる×3, の×3…).
Decisions frozen in `scripts/data/dedup_decisions.json`, applied by
`scripts/apply_dedup.py` (repoints every prereq/fold ref to the survivor, safety-gated
against the curated path), audit `scripts/data/dedup_applied.md`. `qa_grammar_nodes.py`
gained a `--merges` flag (merged high-risk term = covered). QA + `build_slice` + `npm run
build` all PASS.
**BUILD step 3a DONE (2026-06-13):** Content Collection fully materialized. New seeder
`scripts/seed_nodes.py` writes one **tag-layer** `.md` per catalog node from
`grammar_enriched.csv` (identity + #7 tags + DAG prereqs + `sources.volumes`, `noindex:
true`, empty teaching body) — **1,450 seeded, the 8 hand-enriched anchors skipped** (never
overwrites). All **1,458** files now validate against the Zod schema (`npm run build`
PASS); catalog QA PASS with `--merges scripts/data/dedup_decisions.json` (the post-dedup
invocation — CLAUDE.md updated).
**BUILD step 3b-template DONE (2026-06-13):** node-page template
`src/pages/learn/japanese/grammar/[slug].astro` built (ran `/impeccable teach` —
PRODUCT.md/DESIGN.md already complete). Renders the full 9-slot schema in DBJG order
(Header+badges → Builds-on chips → Meaning → Key sentence(s) → Formation → Variants →
Examples → When-you-can't-use → Easily-confused-with → Notes → soft AppCTA → See-also),
single-column mobile-first, DESIGN.md tokens; build-time furigana parser
(`漢字{かんじ}`→`<ruby>`); single-sense↔multi-sense normalized to one render path; per-slot
visual distinction (green key-sentence hero, clay "can't use" callout, indigo "confused
with" comparison). **Decisions (user-confirmed):** stubs render a real "guide coming"
page (noindex, still navigable); prereqs/related = inline-top "Builds on" + footer "See
also"; ad slots reserved (commented) not rendered (AdSense=Phase 4). `noindex` from
frontmatter; JSON-LD Article only when indexed + has content. **All 1,458 pages prerender
+ validate** (`prerender=true`); build ~78s after fixing an O(n²) (resolve nav labels
once in `getStaticPaths`, not per-page). Tree `index.astro` cards now link to node pages.
**BUILD step 3b-Foundations DONE (2026-06-13):** Pass-2 teaching-content fill for the
**entire Foundations line — all 60 nodes** (58 stubs hand-enriched per CALIBRATION2.md;
the 8 form-anchors were already done). Every Foundations node now clears the non-thin gate
(`keySentence`/`senses` + examples + equivalents) and **flipped `noindex:false`** → the
curated trunk indexes immediately. Slot judgment applied per CALIBRATION2 §1–§3 (presence
earned, not defaulted): multi-sense `senses[]` where real (に destination/existence/time,
で place/means/cause/scope, か question/or/embedded, と and/with, ている ongoing/resulting,
てしまう completion/regret, ほしい thing/action, まで endpoint/even, ない negation/existential);
high-value `restrictions` + cross-linked `contrasts` on the confusion clusters (は/が, the
four conditionals と/たら/ば/なら, あげる/くれる/もらう + てあげる/てくれる/てもらう, から/ので,
けど/が/のに, 前に/あとで, だろう/でしょう/かもしれない/はず). All 1,458 pages build PASS,
0 dangling contrast/prereq slugs, multi-sense + sense-pinned restrictions render verified.
A few Pass-1 `confidence` upgrades med/low→high where the meaning was never actually shaky
(datta, de, hoshii, kara, ga-3, ichiban, to-conditional). **Next: step 3b-goals** = Pass-2
fill of the active goal-route nodes (Read-novels branch + any other launched lines), then
long-tail. **step 4** = tree UI pan/zoom.
**BUILD step 3b-goals DONE (2026-06-14):** Pass-2 teaching-content fill for the
**entire Read-novels goal branch — all 22 nodes** (the literary route from the vertical
slice, `register⊇{literary}`). Every node hand-enriched per CALIBRATION2.md, clears the
non-thin gate (key sentence + examples ≥3 + equivalents), and **flipped `noindex:false`**
→ the goal route indexes. Slot judgment applied per CALIBRATION2 §1–§3: multi-sense
`senses[]` where real (まい neg-conjecture/neg-volition, 故に therefore/because-of); high-
value `restrictions` on the form-restricted classics (だに's fixed set, なり same-subject/
spontaneous, べからず/べく irregular せ-, すら negative-polarity, かのごとく counterfactual);
cross-linked `contrasts` on the confusion clusters (である/だ/です, ず/ぬ/ないで,
ねばならない/なければならない, であろう/だろう, 如し/ようだ, のみ/だけ/ばかり, すら/さえ/も,
だに/すら/さえ, つつ/ながら, as-soon-as なり/や否や/途端に/と同時に, と言えども/とはいえ/ても,
ものを/のに, 故に/から/ために, にあって/において, 折に/際に/とき). A few Pass-1 med→high
confidence upgrades where the meaning was never shaky (mai, to-ie-domo); nari kept med
(homograph family) but indexed with a disambiguating note. All 1,458 pages build PASS,
0 dangling contrast/prereq slugs, 0 furigana brace imbalances. **Next: long-tail Pass-2
fill** (remaining ~1,376 stubs, stay noindex until enriched) + **step 4** = tree UI
pan/zoom.
**BUILD long-tail batch 1 DONE (2026-06-14):** Pass-2 fill of the **21 highest-value
essential N5/N4 stubs** (the first long-tail batch — selected by `freq=essential` + low
JLPT for SEO weight per JENGOLANG, not by tree position; 97 essential stubs remain after
this). Thematically clustered so `contrasts` cross-link densely: limiting particles
(だけ/しか, the canonical 'only' pair), comparison/degree (より multi-sense than/from,
ほど multi-sense degree/neg-comparison, ぐらい), desire/intention (がほしい, つもり,
ようと思う), ability/seeming (ことができる, ようだ multi-sense conjecture/resemblance,
やすい), quotation (と/という/と思う), connectives (だから, しかし, そして), and the
obligation/permission/advice quadrant (なければならない/なくてもいい/たほうがいい, all
cross-linked to the already-done てはいけない/てもいい). Slot judgment per CALIBRATION2
§1–§3: multi-sense `senses[]` only where real (より, ほど, ようだ, という); high-value
`restrictions` on the learner-error classics (しか-needs-negative, ほしい-3rd-person→
ほしがる, たほうがいい-past-form, にとって≠のために benefit, ことができる no double-potential);
contrasts seeded from same-`family`. Confidence upgrades med/low→high where meaning was
never shaky (to-quotative, hodo→med). `しかし` register corrected casual→formal/written.
All flipped `noindex:false` (109 indexed now, was 88). All 1,458 pages build PASS,
0 dangling contrast/prereq slugs, 0 furigana imbalances, rendered furigana + multi-sense
verified. **Next: long-tail batch 2** (the remaining ~76 essential stubs, then common) +
**step 4** = tree UI pan/zoom.
**BUILD long-tail batch 2 DONE (2026-06-14):** Pass-2 fill of **15 essential N4/N5 stubs** —
the **obligation / prohibition / advice web + explanatory のだ + polite invitations** cluster,
chosen to cross-link densely into batch-1's already-indexed てはいけない/てもいい/なくてもいい/
たほうがいい/なければならない. Nodes: the "must" family (なければ conditional base +
なければいけない/なくてはいけない/なくてはならない/ないといけない — all four contrasted as
same-meaning-different-base/register, the canonical learner question), advice
(ないほうがいい/ほうがいい — ほうがいい framed as the **comparison** form のほうがいい+より to
differentiate from batch-1's たほうがいい specific-advice), polite prohibition/request
(てはいけません/ないでください), explanatory のだ/んです/のです (のだ = full canonical page w/
`nuance` + overuse `restriction`; んです/のです indexed as register variants per the
darou/deshou precedent), and the invitation trio ましょう/ましょうか/ませんか (cross-linked).
Slot judgment per CALIBRATION2 §1–§3: `restrictions` only where a real learner-error exists
(ないほうがいい keeps ない-form not past; ほうがいい past-vs-nonpast; のだ overuse); `nuance`
fired on のだ/ましょうか/ませんか (connotation a structured field can't carry); no manufactured
slots. **One Pass-1 tag fix:** `nai-de-kudasai` keigo sonkeigo→teineigo (ないでください is
plain polite, not honorific). All flipped `noindex:false` (**124 indexed now, was 109**;
62 essential stubs remain). All 1,458 pages build PASS, 0 dangling contrast/prereq slugs,
0 furigana brace imbalances (pre-build stdlib lint + `npm run build`). **Next: long-tail
batch 3** (62 essential stubs left → then `--freq common`) + **step 4** = tree UI pan/zoom.
**BUILD long-tail batch 3 DONE (2026-06-14):** Pass-2 fill of **14 essential N5/N4 stubs** —
the **existence / becoming / よう-aspect / purpose** web, chosen for dense internal
cross-linking. Nodes: existence (ある/いる + the 〜がある/〜がいる/〜があります constructions —
core teaching point = the **animate/inanimate** split, fired as a `restriction` on each + the
ある↔いる, がある↔がいる contrasts), becoming/deciding (なる + 〜になる・〜くなる + にする — the
canonical **になる/にする** natural-vs-deliberate contrast pair, `restriction` on くなる-not-になる
for i-adjectives), the よう family (**ように** done as a rich **2-sense** node resemblance/purpose
with the ように-vs-ために purpose `restriction`; ようになる/ようにする the なる/する change-vs-effort
pair; **ようとする** 2-sense attempt/about-to), and purpose (ために verb-purpose + のために
**2-sense** benefit/cause). Multi-sense nodes used `senses[]` with sense-pinned
`restrictions`/`contrasts` (e.g. ように purpose-restriction pinned to the purpose sense).
Slot judgment per CALIBRATION2 §1–§3: `restrictions` only on real learner-errors
(animate/inanimate, くなる, ように/ために); `nuance` on なる (natural-change feel); no
manufactured slots. All flipped `noindex:false` (**138 indexed now, was 124**; 48 essential
stubs remain). All 1,458 pages build PASS, 0 dangling slugs, 0 furigana imbalances, all
sense-refs match a senses[].label (pre-build stdlib lint + `npm run build`). **Next:
long-tail batch 4** (48 essential stubs left → then `--freq common`) + **step 4** = tree UI
pan/zoom.
**BUILD long-tail batch 4 DONE (2026-06-14):** Pass-2 fill of **12 essential N5/N4/N3 stubs** —
the **degree / polarity adverbs + demonstratives + sequencing** web, chosen for dense
internal cross-linking. Nodes: the still/already aspect-adverb pair (まだ 2-sense still/not-yet,
もう 2-sense already/not-anymore — contrasted as polar opposites; まだ also linked to the
already-indexed まだ〜ていません), degree (もっと comparative 'more' vs とても absolute 'very' —
mutually contrasted; とても done **2-sense** very / can't-possibly), negative-polarity (全然
needs-negative, 絶対に 2-sense will/won't — 全然↔絶対に↔とても triangulated on what each does with
a negative), the loose adverbs すぐ (variant すぐに + spatial note) / また (2-sense again /
moreover) / 一緒に, the adnominal demonstrative pair この↔こんな (the specific-item vs
type-of-thing contrast, each with the これ/こんなに restriction), and sequencing それから
(contrasted with the batch-1 そして + また). Slot judgment per CALIBRATION2 §1–§3: multi-sense
`senses[]` only where a real polarity/meaning split exists (まだ/もう/とても/絶対に/また);
`restrictions` only on genuine learner-errors (とても〜ない≠'not very'; 全然 needs negative;
この≠これ; こんな vs こんなに); `variants` on 絶対(に)/すぐ(に); `notes` for homonym/series
disambiguation (もう+number='more', こ・そ・あ・ど series) — no manufactured slots. All flipped
`noindex:false` (**150 indexed now, was 138**; 36 essential stubs remain). All 1,458 pages
build PASS, 0 dangling contrast/prereq slugs, 0 furigana brace imbalances, all sense-refs
match a senses[].label, rendered ruby verified in built HTML (pre-build stdlib lint + `npm run
build`). **Next: long-tail batch 5** (36 essential stubs left → then `--freq common`) +
**step 4** = tree UI pan/zoom.
**BUILD long-tail batch 5 DONE (2026-06-14):** Pass-2 fill of **18 essential N5/N4/N3 stubs** —
the **te-form connectives + concession + listing + topic-comment copula + temporal/range** web,
chosen for dense internal cross-linking. Nodes: the te-form connective set (くて i-adj 'is~and',
なくて neg 'not~and/because not', ないで **2-sense** without-~ing / casual 'don't', で copula
te-form 'being~and' = de-3), concession (ても 'even if/though', でも **2-sense** 'even (extreme
example)' / '~or something' particle), representative listing (たり〜たり + the full
たり〜たりする, differentiated by angle — element vs する-closes-and-carries-tense), aspect
(まだ〜ていません 'not yet', linked to te-iru + もう), the topic-comment copula trio (は〜だ plain /
は〜です polite / は〜が theme-with-inner-subject 象は鼻が長い) + じゃなかった casual past-neg, and
the temporal/range set (あとで 'after'=ato-de-2 ↔ 前に, までに deadline ↔ まで/までで, 頃 'around
(time)' ↔ ぐらい 'about (quantity)', から〜まで 'from~to'). Slot judgment per CALIBRATION2 §1–§3:
multi-sense `senses[]` only where a real split exists (ないで, でも); `restrictions` only on real
learner-errors (なくて vs ないで manner; ても+いくら; までに deadline≠まで span; 頃≠ぐらい; は〜が
が-not-を for 好き/できる; あとで needs た-form; だ not on i-adj); `contrasts` densely cross-linked
within and into already-indexed te-mo-ii/te-iru/mae-ni/made. Confidence upgrades where meaning
was never shaky: **te-mo low→high, de-mo med→high, wa-da/wa-desu/wa-ga med→high**. Two seed
fixes: **wa-ga prereq ga-3→ga-2** (subject が, not 'but' が — homograph), **wa-da prereq
desu→da** (X は Y だ). **5 `foldInto` voiced-allomorph/unresolved stubs left `noindex` by
design** (de-iru/de-kudasai/de-mo-ii/de-wa-ikenai → their て-parents; o-unresolved). All flipped
`noindex:false` (**168 indexed now, was 150**; 18 essential stubs remain, ~13 indexable). All
1,458 pages build PASS, 0 dangling contrast/prereq slugs, 0 furigana brace imbalances, all
sense-refs match a senses[].label, rendered ruby verified in built HTML (pre-build stdlib lint +
`npm run build`). **Next: long-tail batch 6** (remaining indexable essential stubs → then
`--freq common`) + **step 4** = tree UI pan/zoom.
**BUILD long-tail batch 6 DONE (2026-06-14):** Pass-2 fill of the **final essential-band stubs** —
the **motion + giving/receiving keigo + embedding/nominalizing** web. **10 indexed:** motion
(へ行く destination ↔ 〜に行く purpose-with-masu-stem — the classic へ-vs-に + destination-vs-purpose
cross-link; 来{く}る done as the irregular-conjugation node, formation table showing the く/こ/き
reading shifts), title suffixes (さん, cross-linked to the already-present 様/ちゃん/君 + the
'never on your own name' restriction), humble receiving (いただく, contrasted with くださる viewpoint
+ ていただく auxiliary + the いただきます note), embedded/nominalizing (かどうか yes/no-whether vs
embedded か with a question-word; 〜方{かた} with the を→の restriction; 連体修飾節 noun-modifying
clause with the inner-subject-takes-が/の restriction), passive 〜られる=rareru-2 (ichidan +
irregular formation, suffering-passive restriction, triangulated against reru/rareru/saseru).
Slot judgment per CALIBRATION2 §1–§3: `restrictions` only on real learner-errors (へ≠static-place;
masu-stem-not-dict before に行く; さん-not-on-self; かどうか-only-yesno + drop-だ; を→の for 方;
inner-subject-が/の; suffering-passive); `contrasts` densely cross-linked to existing nodes; no
manufactured slots. **3 stubs lightly filled but kept `noindex` by design** — ni (bare umbrella),
ni-5 (に point-in-time), shimau (lexical base): each is **redundant with an already-indexed
canonical page** (ni-2 owns destination/location/**time** incl. the absolute-vs-relative-time
restriction; te-shimau owns the auxiliary + ちゃう contraction and lists shimau as its prereq), so
indexing them = duplicate/thin content — exactly the tax the noindex posture exists to avoid
(CALIBRATION2 §1/§2 judgment-over-symmetry). They render as navigable disambiguation hubs pointing
to the canonical page. **5 voiced-allomorph/unresolved foldInto stubs untouched** (de-iru/
de-kudasai/de-mo-ii/de-wa-ikenai/o-unresolved). Confidence upgrade: **kuru med→high** (verb meaning
never shaky). All flipped `noindex:false` for the 10 (**178 indexed now, was 168**). All 1,458 pages
build PASS, 0 dangling contrast/prereq slugs, 0 furigana brace imbalances, all sense-refs match,
rendered ruby verified in built HTML (pre-build stdlib lint + `npm run build`). **Essential band
drained** (8 essential stubs left = the 5 foldInto + 3 noindex hubs, all intentional). **Next:
`--freq common` (batch 7)** + **step 4** = tree UI pan/zoom.
**BUILD essentials-finish pass DONE (2026-06-14):** drained the last 8 essential stubs to **0
pending** (178 → **182 indexed**). **4 indexed:** ni (reframed as an *all-roles-of-に* roundup/hub
— a distinct SEO target, not a per-sense dup), ni-5 (focused *に with time expressions* — deeper than
ni-2's single time sense: absolute-vs-relative restriction, frequency 一日{いちにち}に二回{にかい}, までに
deadline contrast), shimau (the lexical verb しまう put-away/close, distinct from the てしまう auxiliary),
and de-wa-ikenai (**de-fold**: removed its `foldInto`, indexed for its genuine noun/na-adj
copula-prohibition sense 〜ではいけない 'must not be ~', which te-wa-ikenai [verb prohibition] doesn't
cover; prereq de-3). **4 stay noindex by design, properly resolved:** de-iru/de-kudasai/de-mo-ii are
pure phonological で-voicings of ている/てください/てもいい → the voicing rule is now documented as a
`note` on each て-parent (te-iru/te-kudasai/te-mo-ii) and the child is a clean noindex redirect-hub
(equiv + key sentence + contrast→parent); o-unresolved is an unrecoverable OCR fragment (canonical="")
left folded into を. **Tooling:** `list_stubs.py` gained `--include-folds`; by default it now **excludes
`foldInto` nodes** (a folded form is not pending Pass-2 work) so the worklist reflects genuine work —
`--freq essential` reads 0. All 1,458 pages build PASS, 0 dangling slugs, 0 furigana imbalances, lint
clean. **Next: `--freq common` (batch 7)** + **step 4** = tree UI pan/zoom.

---

---

## Status & next session (2026-05-30)

**Pilot done.** The enrichment pilot confirmed the catalog is AI-recoverable: the
failure mode is OCR garble, not unknown grammar. Prep step built (`prep_grammar_nodes.py`)
→ **`grammar_nodes.csv`** = **1,090 candidate nodes**, of which **64 collision-risk +
20 garble-risk** are auto-flagged as the judgment-heavy worklist; ~1,006 are clean.

**Execution decision (changed):** enrichment is done **by Claude in-session via this
chat interface — NOT the API.** The Anthropic API key in `JengoApp/.env` has no
credits, and the user prefers the in-session hand-pass anyway (full review, asks
questions on ambiguity). The Batch-API pipeline (`enrich_grammar_nodes.py`) is built
and validated up to the billing wall — **parked as a fallback** if credits are added.

**DONE so far:** high-risk pass **98/98** → `grammar_enriched.csv` (106 records, QA PASS).
`CALIBRATION.md` frozen. `qa_grammar_nodes.py` built. Clean pilot (23 source terms →
`grammar_enrich_pilot.csv`, throwaway, pre-/overlap notes below).

**Scripts (in `JengoApp/scripts/`):** `prep_grammar_nodes.py` (catalog→worklist, regex
bug fixed), `qa_grammar_nodes.py` (QA, done), `enrich_grammar_nodes.py` (API enrichment,
parked on billing).

---

## ► CLEAN-PASS HANDOFF (next session — start here)

**Goal:** enrich the remaining **992 clean + 53 missing_only** rows of
`grammar_nodes.csv` into `grammar_enriched.csv`, applying **`CALIBRATION.md`** (the
frozen spec — read it first). "Clean" ≠ easy: the pilot measured **~42% need judgment**
and ~980/1,006 rows have NO English gloss (reconstruct meaning from romaji + see-also +
volume). Apply the collision guard to **every** row.

**Step 0 — reconcile the pilot.** The 26 pilot records were written **before** the
homograph-regex fix. Three are now superseded by homograph-aware nodes in the main file
and must be **dropped/redone**, not merged blindly: pilot `iru-3` (要る) → main has
`iru-4`; pilot `kureru` (くれる) → main has it; pilot `nante-2`. The other ~23 pilot
records are good clean work — fold them in (and add `review_reason` to pilot rows
`nai-de-mo-nai`, `ni-itatte-wa`). Easiest: delete the pilot file and re-enrich its 23
terms inside the normal clean order so nothing is special-cased.

**Step 1 — execution: LOCKED = (B) single-thread in-chat** (user chose consistency over
speed, 2026-05-30). One model the whole pass — **Opus** (the ~42% reconstruction-judgment
rows want the strong model; switching models mid-pass is the cross-model variance we're
avoiding). Sonnet single-thread is the only sanctioned fallback if session-count must drop.
Naive agent fan-out was rejected (42%-judgment + latent collisions). Caps below.
**Cost:** in-session = ~6 sessions on the subscription (no per-node $); the parked Batch
path would be ~$3 Sonnet / ~$14 Opus total if credits are ever added.
Catch-net regardless: **run `qa_grammar_nodes.py`**, then spot-read ~15%.

**Step 2 — enrich** (resumable; cursor = `grammar_enrich_progress.json`, set `mode:"clean"`).
  - Fixed order: clean rows **by term**. Read only your slice (offset/limit) — never the
    whole CSV.
  - **Append** to `grammar_enriched.csv`; flush every ~25 rows so compaction loses ≤1 chunk.
  - **Re-anchor every ~50 rows:** restate the CALIBRATION freq/family rubric.
  - **Slugs must be globally unique** — check against existing slugs before writing
    (cross-pass clash already seen: `nante`).

**Step 3 — QA + resolve.**
  - `python3 scripts/qa_grammar_nodes.py grammar_enriched.csv [shards…] --source grammar_nodes.csv`
    → must be PASS (0 hard). Fix dangling prereqs; pending prereqs auto-resolve as nodes appear.
  - **Prereq-resolution fix step:** once the clean pass is complete, flip any still-unresolved
    bare prereq slugs to `*` (non-catalog foundation) — these are the `*te-form`/`*nai-form`
    type anchors. (`te-mo`, `dake`, `bakari`, `koto`, `to-shite` should all become real nodes.)

**Step 4 — then:** external-source reconciliation (#15: Bunpro/Tae Kim/JLPT — catch
sense-collisions, fill DBJG gaps, re-check the 22 low-confidence high-risk nodes), then
build **one vertical slice** (Foundations line + one branch, fully tagged) to validate
the model before the tree UI.

**Calibration question RESOLVED (2026-05-31): KEEP.** Lexical / borderline-lexical
items stay as nodes. Per CALIBRATION §2: keep grammar senses; an entirely-lexical row
→ `fold_into_parent` + `freq=rare`, `jlpt=none`, `conf=low`, review note — **never
deleted**. Borderline adverbs (明らかに/案外/中途半端) kept as `adverbial` with a review
note. Reversible later with one filter on `fold_into_parent`/review_reason.

## Session batching rule (avoid context rot)

In-chat enrichment drifts (inconsistent freq/family/confidence) and risks compaction
long before the 1M window fills. Cap each session by *working enrichment tokens*, not
the hard limit. Footprint ≈ **~300 tokens/clean node**, **~700/high-risk node** (incl.
sense reasoning + user Q&A).

**Per-session caps (whichever hits first):**
- **High-risk pass:** ≤ **50** nodes/session (judgment-bound, not token-bound). 84 total → ~2 sessions.
- **Clean pass:** ≤ **175–200** nodes/session (~250 only if calibration still feels stable). ~1,006 → ~5–6 sessions.
- **Hard backstop:** if working context nears **~150K tokens**, finish the current chunk and stop regardless of count.
- Total job ≈ **7–9 sessions**.

**Protocol (makes sessions resumable + drift-resistant):**
1. **Fixed order:** all `risk != ""` rows first (by term), then clean rows (by term).
2. **Read only your slice** of `grammar_nodes.csv` (offset/limit) — never load all 1,090 (~87K tokens wasted).
3. **Append** results to `grammar_enriched.csv`; flush every **25 clean / 10 high-risk**
   so compaction never loses more than one chunk.
4. **Cursor file** `JengoApp/scripts/ocr_output/grammar_enrich_progress.json` =
   `{mode: "risk"|"clean", last_term, done_count, total}` — update on every flush; next
   session reads it first and resumes after `last_term`.
5. **Re-anchor every ~50 nodes:** restate the tag rubric briefly to fight calibration drift.
6. **Session end:** update this block's status line with the cursor (e.g. "risk pass 50/84 done,
   resume after `noni`").

**Model:** **Opus** drives the 84 high-risk nodes (collision guard #14 is judgment
the strongest model does best); reassess Opus-vs-Sonnet for the ~1,006 clean bulk
after calibration is seen to hold (drift-resistance #72-rule vs. cost).

**Enrichment cursor:** risk pass **COMPLETE 98/98**. Clean pass **COMPLETE
967/992 terms done** (2026-06-02), cursor `mode:"clean"`, `last_term="ǎ shita"`.
The 25-term gap to 992 is **all intentional cross-row-dup drops** (their pattern
lives under another slug) — 10 from Session 6 (`toka 2 toka`, `~tokatoka`,
`towazu o towazu`, `wa oroka`, `wake ga nai`, `yori/no hoka…`, `yoru to ni yoru to`,
`~ba~hodo`, `~de are- de are`, `~mo mo`) + 15 from earlier sessions (hazu ga nai,
te mo, te miru, te kudasai, tatte, to ie domo, to shite mo, no da, etc.). Output
`grammar_enriched.csv` = **1,075 records**, QA **PASS** (0 hard, 0 dangling, 0
unresolved bare prereqs — `tokoro`/`yue-ni` now enriched and resolved). Confidence
dist: 640 high / 320 med / 115 low. Session 1 covered `(datta)`→`desu` (256 recs);
Session 2 `dochira ka to ieba`→`kiraida` (+175); Session 3 `kitto`→`nasu` (+175,
K→N, `/effort medium` — no calibration change); Session 4 `naze ka`→`sei` (+168,
N→S: the に〜/の〜/を〜 formal-connective spine + s-starters); Session 5
`sekkaku`→`to wa kagiranai` (+175, S→T: て-form auxiliary/aspect family + そ-discourse
connectors + と〜 quotative/connective spine); **Session 6 covered `toka`→`ǎ shita`
(+126, T→end, run on `/effort high`)**: the とき/ところ temporal-nominalizer cluster,
the は〜 topic-frame + concessive spine (はさておき/は別として/は言うまでもなく), the
よう/ように volitional+manner family (resolved the long-pending `*youni` anchor), the
ず classical-negative spine (ずに/ずにはいられない/ずして/ずとも), and the `~X~Y` paired-
listing family (たり〜たり, か〜か, やら〜やら, でも〜でも…). **Clean pass done →
proceed to Step 4 (external-source reconciliation, then build one vertical slice).**
Helper
`scripts/append_enriched.py` (validates enums + global slug-uniqueness, appends,
advances cursor) — feed it a JSON batch + the new last_term.
Clean-pass notes for next session: (a) many て→で voiced allomorphs (であげる/でいる/
でおく…) were emitted with `fold_into_parent` = their て-form parent slug (te-ageru,
te-iru…) — those parents land under 't', will resolve then; (b) the `dake de (wa)
naku` family already has 7 near-dup rows (slugs `dake-de-wa-naku-3..7`) all flagged
merge; expect more cross-ref dups; (c) lexical question (CALIBRATION §2) handled
conservatively — borderline adverbs (明らかに/案外/中途半端) kept as `adverbial` with a
review note, never deleted; (d) pending prereqs `koto`/`nara`/`to-shite` are real
upcoming terms — leave as-is, they auto-resolve.
**Session 2 learnings:** (e) **slug macron convention = `ou`/`uu`** (ō→ou, ū→uu,
matching existing deshou/darou) — but `qa_grammar_nodes.py` `slugify()` *drops*
macrons (yōni→"yni"), so a prereq pointing at an unenriched よう-family node can't
be auto-classified as pending and shows as a hard `dangling`. Workaround used:
`*`-prefix it (`*youni`), which the Step-3 post-pass reconciles to the real node
once 'y' is enriched (same pattern as `*to-quotative`→`to-quotative`). (f) Genuine
non-catalog foundations must be `*`-prefixed (`*counter`, `*ba-conditional`,
`*ta-form`) or QA hard-fails. (g) Cross-pass dup hit: `hazu-ga-nai` already existed
from the risk pass (term "Vpot hazu ga nai") — dropped my clean dup. (h) Many
OCR-`2`-artifact / repetition garbles in D–K reconstructed conservatively at
`conf=low` with merge notes (`ichi-to-shite-nai`, `kanarazushimo-nai`,
`kesshite-nai`, `ni-kimatte-iru`, `ni-kakete-wa`, `ju-made-mo-nai`).
**Session 3 (K→N, kitto→nasu) learnings:** (i) **effort level is irrelevant to
this pass** — judgment is fixed by the frozen CALIBRATION rubric + collision guard,
so `/effort medium` only set the per-session *count* target (aimed the lower ~175
end of the cap), not per-node rigor. Reported to user. (j) Heavy near-dup clusters
in this slice (`mono(da)`×2→mono-da/mono-da-2, `nashi de(wa)`/`nashi de wa`→
nashi-de-wa/nashi-de-wa-2, `nashi ni(wa)`/`nashi ni wa`→nashi-ni-wa/nashi-ni-wa-2,
`nai koto mo nai`/`mo/wa nai`, `nani-nai`/`nanra-nai`, `mottomo`→split 最も vs
concessive もっとも) — all kept distinct with `-N` suffix + dup-suspect review note
per CALIBRATION (no cross-row merge in-pass). (k) Two cross-row dups already enriched
in earlier passes were **dropped, not re-created**: `ni-koshita-koto-wa-nai` (risk
pass) and slug `nante` (→ used `nante-2` for the exclamatory sense). (l) Same macron
issue as Session 2: prereq `youni` (よう-family) hard-failed QA because slugify drops
ō; `*`-prefixed to `*youni` for the Step-3 post-pass. (m) Lexical/borderline rows
kept per §2 with conf=low + fold/drop note (`kiraida` already there; `nasu` 成す,
`motte-iru` 持っている→folds into te-iru). QA PASS 0 hard after the youni fix.
**Session 4 (naze ka→sei) learnings:** (n) This slice is dominated by the formal
**に〜/の〜/を〜 grammaticalized-connective spine** (に対して, に関して, によって,
をめぐって, を通じて, をはじめ…) — almost all clean N2/N1 `connective`/`particle`,
mostly `conf=high`. (o) Many `/`-slash source terms are te-form + adnominal of one
pattern (`ni hanshite/hansuru`); primary slug = first variant, the adnominal →
`-2` dup-suspect (ni-hanshite-2, ni-kanshite-2, ni-taishite-2). (p) The によって
family had **4 OCR dup rows** → ni-yotte (primary) + ni-yotte-2/3/4 (conf=low,
dup-suspect). (q) **6 cross-row dups dropped or renamed at append time** (QA caught
them as slug clashes vs earlier passes): dropped `ni-koshita-koto-wa-nai`, `no da`
(=existing no-da 'In da'), `ni-hikikae`, `ni-kimatte-iru`, `ni-shita-tokoro-de`,
`no-nan-no-tte`; **emotive を renamed `o-3`→`o-4`** (o/o-2/o-3 already = object/path/
separation を — emotive ものを is a distinct 4th sense, kept). (r) OCR-fused garbles
reconstructed at conf=low: `ni-kankei-naku` (←"ni ni kankei kakete naku wa"=に関係なく),
`okinji-enai` (←を禁じ得ない, dropped を head), `o-oite-hoka-ni-wa-nai` (stray '2'),
`wa-oroka` (←"oroka wa oroka"=はおろか; merge w/ any W-pass row), `oda` (unrecoverable,
fold→no-da, candidate drop). (s) Lexical-fold per §2: `negau`, `okonau` 行う,
`o-kinzuru` 禁ずる kept conf=low with drop-candidate notes (never deleted).
**Session 5 (sekkaku→to wa kagiranai) learnings:** (t) **PREREQ SEPARATOR IS `|`,
NOT comma** — `append_enriched.py` does not validate prereq syntax, so 8 comma-joined
prereqs slipped through and QA hard-failed as `dangling` (the whole `"tai,te-mo"`
read as one slug; `*`-leading comma-joins were silently *skipped*, masking the bug).
Fixed by replacing `,`→`|`. Use `|` for every multi-prereq from now on. (u) Big
clean families landed here: the て-form spine (てあげる/てくれる→te-kudasaru/てもらう/
ていただく auxiliary; ている/てある/ておく/てしまう aspect; てはいけない/てもいい/てほしい
modality) — most `essential`/`common`, `conf=high`; **te-iru and shimau enriched →
resolved two long-standing pending prereqs**. (v) **6 cross-row dups dropped** (already
enriched earlier): te-mo, tatte, te-kudasai, te-miru, to-ie-domo, to-shite-mo. (w)
Internal `-2` dup-suspects kept per CALIBRATION (no in-pass merge): taku-to-mo-nai/-2,
takute-mo-nai/-2, tame-ni/-2, tara-sugu/-2, sono-ue/sono-ue-ni, sukoshi-mo/-nai,
to-iu-yori/-wa, to-iu-fu-ni/to-iu-you-fu-ni/to-iu-youni. (x) Macron slugs follow the
ou/aa convention (souda, saa, sou-ka-to-itte, to-douji-ni, to-iu-youni); none are
referenced as bare prereqs so no slugify-drop hard-fail this slice. (y) One
unrecoverable OCR row left conf=low canonical="": `to-itsu-de-mo` (gloss→度に). (z)
Lexical-fold/borderline per §2: shiru 知る (kept for 知っている), sukida 好きだ, sukunai
少ない, takusan, sumaseru/sumu — conf med/low with notes, never deleted.
**Session 6 (toka→ǎ shita, T→end — FINAL clean slice) learnings:** (aa) **10
cross-row dups dropped** (pattern already enriched under another slug, never
re-created): `toka 2 toka`/`~tokatoka`→toka-toka, `towazu o towazu`→o-towazu,
`wa oroka`→wa-oroka, `wake ga nai`→wake-ga-nai, `yori/no hoka…`→yori-hoka-nai,
`yoru to ni yoru to`→ni-yoru-to, `~ba~hodo`→ba-hodo, `~de are- de are`→de-are-de-are,
`~mo mo`→mo-mo. Verified against the existing-slug set *before* writing — caught
them up front rather than at append. (bb) Internal `-N` dup-suspects kept per
CALIBRATION (no in-pass merge): bakari-de-wa-naku-4, dake-de-wa-naku-8/9,
tari-tari-2, tari-tari-suru-2, yara-yara (vs yarayara), you-ni-mo-nai/-2,
yaya-mo-sureba/-suru-to, yahari/yappari/yahari-yappari, zenzen/zenzen-nai,
totemo/totemo-nai, wa-are/wa-atte-mo, wa-ikenai/wa-naranai, wa-da/wa-desu. (cc)
**`youni` enriched as a rich multi-sense node (resemblance/purpose/manner) →
resolved the long-pending `*youni` anchor** referenced by yona/yoni-so-that; also
enriched tokoro, yue-ni, shimau-adjacent ず-family. (dd) Macron convention held
(ou/oo/aa): you-*, oomune, oozei, aa-shita; ǎ→ああ (aa-shita), ō→おお (oomune 概ね)
vs ō→おう (you- volitional) disambiguated by the actual word. (ee) Bare-romaji
listing patterns `~X~Y` reconstructed as family=particle, mostly uncommon/rare,
conf med/low (ga-nara, ni-nai, wa-wa lowest). (ff) Lexical-fold per §2: wakeru
分ける, oozei 大勢 kept conf=low family=other with "candidate to drop" notes, never
deleted. (gg) **append_enriched.py path quirk:** run the builder with the source
path as `ocr_output/grammar_nodes.csv` (cwd=scripts/); pass QA `--source
grammar_nodes.csv` (basename only — it resolves relative to the enriched file's
dir). (hh) **Final QA: PASS, 0 hard, 0 dangling, 0 unresolved bare prereqs.**

---

## Step 4a — External-source reconciliation (PASS 1 DONE, 2026-06-02)

The #15 catch-net. Compared all **1,075 enriched nodes** against external grammar
references; QA still **PASS** (0 hard) after all edits. Scripts in `JengoApp/scripts/`.

**Reference built** (`ocr_output/`):
- `bunpro_deck_index.json` — **910** Bunpro grammar points, JLPT-tagged (N5–N1), the
  primary form-match + level source. (Downloaded from the public wkanki GitLab mirror.)
- `jlpt_grammar_ref.csv` — **696** JLPTsensei points (japanese/romaji/meaning/level),
  scraped by `fetch_jlpt_grammar.py`. Adds the English glosses Bunpro lacks (collision
  check). N5:76 N4:128 N3:156 N2:156 N1:180. *jlptsensei rate-limits hard — N2 p4 (~37
  rows, o-/sa- forms, redundant w/ Bunpro) was unreachable; the rest came via WebFetch.*
- Tae Kim's 62 lesson topics (in `bunpou/japanese-grammar-db`) = conceptual checklist
  for the Foundations line; lesson-title level, not form-matchable.

**Matching** (`reconcile_external.py`): Japanese-form↔Japanese-form with tolerant
variant normalization (strip 〜/～, split `/`・ alternatives, paren-optional, circled-
number ①② + superscript markers) **plus** a romaji→slug axis (our slugs are romaji).
Outputs `grammar_gap.csv`, `grammar_jlpt_diff.csv`, `grammar_match_report.csv`.
`triage_reconcile.py` → `grammar_gap_triaged.csv` (categorized) + `grammar_jlpt_fix.csv`.

**Findings:**
- **Coverage:** 601/1,075 of our nodes are externally validated; the other **474 are
  DBJG-unique** (rare/literary/classical long-tail — expected per decision #2).
- **Gaps (#15b, fill DBJG lacks):** **635 distinct** external points not in our tree.
  After triage: **519 grammar_candidate** (N1:176 N2:109 N3:111 N4:88 N5:35), **139 of
  which appear in BOTH sources** (highest-confidence add list); the rest = 78 structural
  labels, 12 demonstratives, 14 short-particle, 12 bare-kanji vocab (out of scope).
  → **This is the next enrichment batch** (see Step 4b). Verified zero false-gaps on a
  spot-check (に過ぎない→ni-suginai, つつ→tsutsu match; あっての/がてら/こととて genuinely absent).
- **JLPT-badge fixes (#15a):** **85** corrections applied where Bunpro+JLPTsensei agree
  on a level unambiguously different from ours (magnitude-1 + 2 verified jumps), audit in
  `grammar_jlpt_applied.csv`. E.g. `iru` ている N3→N5, `darou` N4→N5. JLPT is badge-only
  (#6) so this is safe; freq/family/meaning untouched.
- **Sense-collisions caught (#14/#15a):** `you` (advanced 〜よう(が/に) wrongly form-matched
  volitional よう), `yori-2` (lexical 寄り vs comparative より), `toka` (listing vs hearsay
  とか（で）), plus `ni-shite-2` (external にして='at certain conditions' ≠ our 'both~and').
  Routed to `grammar_collision_suspect.csv` / flagged in review_reason — NOT auto-changed.
- **22 low-conf high-risk nodes re-checked** (`recheck_low_conf.py`): 15 externally
  confirmed → low→med (conf dist now **640 high / 335 med / 100 low**); 7 correctly stay
  low (lexical 要る/寄り/やる/自分, dup `noni-3`, ambiguous `o-unresolved` folded into `o`).

## Step 4b — Remaining (next sessions)

1. **Gap-fill enrichment** of the 519 grammar_candidates.
   - **DONE (2026-06-02): 139 dual-source (Bunpro+JLPTsensei) candidates enriched** →
     appended to `grammar_enriched.csv` (now **1,215 records**, QA PASS, 0 hard/soft/
     dangling). These had JLPTsensei glosses so reconstruction was easy; almost all came
     back `conf=high`. Slice was N1:33 N2:44 N3:35 N4:20 N5:7. Notes: 4 `med` rows
     (denakute-nan-darou, kare-kare, dake-wa, no-mo-mottomo-da); honorific/humble rows
     tagged keigo (de-gozaimasu/gozaimasu=teineigo, irassharu/nasaru=sonkeigo,
     te-itadakemasen-ka=kenjougo); gap-fill rows carry `src_risk=gapfill`,
     `src_volumes=ext`, `src_glosses`=the external gloss for provenance. Foundation
     prereqs use `*te-form`/`*nai-form`/`*masu-stem`/`*ta-form`/`*ba-conditional`/
     `*volitional-form`; intra-batch prereqs (ni-kagiru, kara-miru-to, kiru, gozaimasu,
     te-iru, etc.) resolve. **One gotcha:** てもいい's existing slug is `te-mo-ii`
     (not `temo-ii`) — check `_used_slugs` before referencing.
   - **DONE (2026-06-02): the 380 single-source candidates** → 2 more batches.
     **(1b) JLPTsensei-only (153 rows, had glosses):** 150 enriched, 3 dropped as dups of
     the dual-source batch (janai / mitai-na→mitai-ni / temo-ii-desu→te-mo-ii). **(1c)
     Bunpro-only (227 rows, NO gloss → reconstructed from the Japanese form):** 156
     enriched, **71 dropped as dups** — these grammar points were already enriched in the
     original clean pass under a kanji/kana variant the reconciler's matcher missed
     (e.g. ながらに/からある/にとって/即ち/却って/と共に/遂に/必ずしも…). **Dedup method that
     worked:** normalize-compare each candidate's Japanese against existing
     canonical+reading (strip 〜～()・), then a second pass where `append_enriched.py`'s
     slug-uniqueness catch flags any kanji-vs-kana slug clash before writing. Reconstruction
     confidence was high — these are clean Bunpro forms, not garbled OCR. **Net: all 519
     candidates processed → 445 enriched + 74 already-covered dups dropped.**
2. **Resolve the 4 collision-suspects** — **DONE (2026-06-02).** `you` (kept N2; external
   N5 = volitional よう, a separate node), `yori-2` (kept lexical 寄り; external = comparative
   particle より = node `yori`), `ni-shite-2` (kept "both~and"; external "at age/condition"
   maps to node `ni-shite` sense 1) — all annotated as false external form-matches in
   `review_reason`. `toka` was a genuine multi-sense → **split: new `toka-2` node** for the
   hearsay 〜とか(で) (N2, family=quotation); `toka` stays listing/vague (N4). Resolutions
   logged in `grammar_collision_suspect.csv` (`resolution` column).
3. **Build one vertical slice** — **DONE (2026-06-03).** Foundations line (60 nodes,
   9 stages) + 8 materialized form-anchors + the Read-novels literary branch (22-node
   curated route over the 145-member `register⊇{literary}` filter). Generator
   `scripts/build_slice.py` → `src/data/grammar_slice.json` (in-repo since 2026-06-05;
   see SLICE.md Artifacts); static render at `/learn/japanese/grammar`. Validation
   **PASS** (82/82 slugs resolve, 0 dangling, 0 ordering violations). **Three IA findings
   in `SLICE.md`:** (a) prereq-depth (#6) collapses to ≤2 tiers — the curated **stage**
   (#9) is the layout axis, prereq edges become the faint mesh; (b) the `*`-form anchors
   are referenced 225× and must be promoted to real nodes/pages; (c) a same-surface
   dedup/sense review (て/te-2 dup vs が-subject/が-"but" split) is needed before the full
   tree — not mechanically separable. The subway-line model (#10) worked with **no new
   data model**; the register **set** tag earned its complexity.

**Prior cursor (risk):** risk pass **COMPLETE 84/84**, then +14 (regex fix) = 98/98.
Output `JengoApp/scripts/ocr_output/grammar_enriched.csv` = **92 records** (8 splits:
amari-2, datte-2, kagiri-2, kara-2, no-2, suru→o-suru/ga-suru, to→to-conditional/
to-quotative, yō→you/you-2). Confidence: 28 high / 45 med / 19 low. No duplicate slugs.
**Worklist correction:** high-risk = `risk ⊇ {collision,garble}` = **84** (the 53
`missing_only` rows are NOT high-risk — they fold into the clean pass).
**`CALIBRATION.md` written** (frozen enrichment spec — rules + romaji-reconstruction
discipline + worked examples). **Clean pilot done** (25 rows → `grammar_enrich_pilot.csv`):
**58% high / 42% need judgment** (15h/8m/3l). "Clean" = no OCR flag, NOT mechanical —
~980/1,006 rows have no English gloss, so the model reconstructs meaning from romaji +
see-also + volume. 4 latent issues found in 25 rows: hidden multi-sense (`koto`),
unflagged `¹³⁴` superscripts (`iru³`/`kureru¹`), cross-pass slug clash (`nante`→nante-2),
cross-row dup (`dake de naku`). **Agent verdict:** disciplined fan-out only — agents need
CALIBRATION.md + see-also index + used-slug list + strong model (Opus/Sonnet, never
Haiku) + scripted QA + ~15% spot-read. Naive fan-out unsafe (42%-judgment rows).

**BUG FIXED (2026-05-30):** `prep_grammar_nodes.py` `HOMOGRAPH_RE` now matches the full
superscript range `¹²³⁴⁵⁶⁷⁸⁹⁰`. Re-ran prep (non-destructive, still 1,090 nodes):
collision 64→78, high-risk **84→98**. The 14 newly-surfaced rows (de³, iru¹/³, ka/ka¹,
kureru/kureru¹, kuru¹, mono ka¹, ni¹/³, noni¹, o³, yaru¹) were then enriched — **high-risk
pass now COMPLETE 98/98 → 106 records** (38h/46m/22l, no dup slugs). Several resolved
earlier ambiguities (mono ka¹ "definitely not" pins emphatic ものか; iru¹ "exist"/iru³
要る "need" separate the conflated iru family). Clean pass to-do: **992 + 53 missing_only**.

### Calibration rules (harvested from the 84 high-risk nodes — seed for CALIBRATION.md)
1. **Potential → `family=modality`** (not `passive`); spontaneous/honorific られる → `honorific`; plain passive → `passive`. One romaji `rareru` legitimately becomes 3+ nodes by superscript.
2. **Vocab-sense drop:** when a polysemous term mixes grammar + lexical senses (suru 'do', ya 'store'/屋, iku 'go', yori 'side'/寄り, morau 'receive'), KEEP only grammar senses as nodes; a node that is *entirely* lexical → `fold_into_parent` + `freq=rare`, `jlpt=none`, `conf=low`.
3. **Auxiliary vs aspect:** benefactive てあげる/てくれる/てもらう/てやる = `auxiliary`; directional/temporal ていく/てくる/ている/てある/たことがある = `aspect`.
4. **No-gloss homograph pairs** (soko de'/², yaru/²): both senses known but the '/² → sense mapping is unrecoverable from the row → assign best-guess, `conf=low/med`, name the guess in review_reason.
5. **Merged-garble rule:** when QA `merged_suspect`/`unbalanced` fuses several patterns into one term, reconstruct + keep the PRIMARY pattern, set `conf=low`, and list the fused-in patterns in review_reason ("others need own nodes") so reconciliation re-adds them.
6. **`~2` prefix = the dictionary's homograph² of a shared base** (e.g. `~2 bakari de naku`) — pair it to node 1 via prereq + flag possible merge; don't treat as unrelated.
7. **Prereq slugs are best-effort:** write the plausible slug; `*`-prefix only known non-catalog foundations (te-form, nai-form, ba-conditional, volitional-form, counter). A post-pass resolves every prereq slug against the final node set and flips unresolved bare slugs to `*` (e.g. `to-quotative` started as `*to-quotative`, later became a real node).
8. **Particle `freq`:** core case/topic particles (は theme, が subject, を object, に dest/IO, で means/place, と 'and', も 'also', から 'from') = `essential`, `N5`; their advanced/contrastive/literary uses = separate nodes at `common`/`uncommon`. `freq` is real usefulness, NOT JLPT (JLPT is its own tag).

---

## PASS.md frontier ledger — archived 2026-07-02

Moved verbatim out of PASS.md §1 (it had grown to ~1,450 lines, defeating the
"slim cursor" purpose). Contains the per-batch indexed-count arithmetic and the
full batch 6–119 narratives. New batch narratives append below this section.

- **Indexed: 1192 nodes** (actual working-tree grep `noindex: false`; reconciled at batch 58 to
  669+29=698, then +21=719, +12=731, +13=744, +10=754, batch 63 +10 = 764, batch 64 +18 = 782,
  batch 65 +17 = 799, batch 66 +18 = 817, batch 67 +5 = 822, batch 68 +2 = 824, batch 69 +1 = 825,
  batch 70 +17 = 842, batch 71 +17 = 859, batch 72 +1 = 860, batch 73 +2 = 862, batch 74 +18 = 880,
  batch 75 +14 = 894, batch 76 +4 = 898, batch 77 +2 = 900, batch 78 +13 = 913, batch 79 +11 = 924, batch 80 +5 = 929, batch 81 +4 = 933, batch 82 +7 = 940, batch 83 +7 = 947, batch 84 +3 = 950, batch 85 +2 = 952, batch 86 +1 = 953, batch 87 +1 = 954, batch 88 +2 = 956, batch 89 +3 = 959, batch 90 +3 = 962, batch 91 +2 = 964, batch 92 +2 = 966, batch 93 +2 = 968, batch 94 +3 = 971, batch 95 +3 = 974, batch 96 +2 = 976, batch 97 +2 = 978, batch 98 +2 = 980, batch 99 +5 = 985, batch 100 +4 = 989, batch 101 +8 = 997 [grep 996], batch 102 +7 = 1004 [grep 1003], batch 103 +7 = 1011 [grep 1010], batch 104 +9 = 1019 [grep 1019], batch 105 +7 = 1026 [grep 1026], batch 106 +5 = 1031 [grep 1031], batch 107 +4 = 1035 [grep 1035], batch 108 +4 = 1039 [grep 1039], batch 109 +3 = 1042 [grep 1042], batch 110 +21 = 1063 [grep 1063], batch 111 +19 = 1082 [grep 1082], batch 112 +11 = 1093 [grep 1093], batch 113 +8 = 1101 [grep 1101], batch 114 +26 = 1127 [grep 1127], batch 115 +14 = 1141 [grep 1141], batch 116 +9 = 1150 [grep 1150], batch 117 +14 = 1164 [grep 1164], batch 118 +14 = 1178 [grep 1178], batch 119 +14 = 1192 [grep 1192]). Done:
  Foundations 60/60 · Read-novels branch 22/22 · essential
  band **fully drained** · common batches 1–5 (adverbial family, largely drained) · **batch
  6** (appearance/evidentiality modality, 8 + 1 redirect) · **batch 7** (necessity/obligation,
  9) · **batch 8** (はず/わけ/べき expectation-logic, 13) · **batch 9** (こと decision/outcome/
  experience, 11) · **batch 10** (keigo verbs + こそあど 連体詞, 18: いらっしゃる/なさる・いたす・
  さしあげる・くださる・お〜になる↔お〜する・お〜ください・ございます/でございます・なさい; こそあど
  こういう↔そういう↔このような・どのような・こうした↔こういった) · **batch 11** (benefactive
  て-grid + connectives, 14): ていただく↔てくださる・てくれない↔ていただけませんか・てもらいたい↔
  てほしい・てやる(2-sense); それで/それでは/それでも/それなら; だけど→けれど→だが · **batch 12**
  (aspect/phase + causative/passive/potential/perception, 29 = 26 indexed + 3 noindex redirects):
  始める↔出す↔終わる・続ける; ておく↔てある; ているところ↔たところ↔るところだ (ところ trio) ↔たばかり;
  ていく↔てくる (2-sense mirror); ていた; なくなる; ちゃう/ちまう/とく → parents; せる↔させる↔させられる・
  させてください; れる↔られる(passive/potential/honorific 3-way ら-shape); られない; 見える↔見られる↔
  が見られる・聞こえる (perception: natural-sense vs opportunity-potential). · **batch 13** (quotation/
  report + nominalizers, 15): ということ↔ということだ(2-sense)・と聞いた・と言ってもいい; the **reported-belief
  trio** と言われている (general saying) ↔ とされている (established/rule) ↔ と考えられている (reasoned/
  expert) mutually contrasted; って(2-sense quotative/topic); nominalizers の(2-sense pronoun/
  nominalizer)・の-2(sentence-final explanatory)・のこと・のは〜だ cleft・もの(↔こと)・さ(degree)・連用形名詞
  用法 — anchored to enriched という/と/こと/のだ/そうだ/らしい. · **batch 14** (conditionals, 12):
  なかったら (negative たら); the **negative-copula "unless" family** でないと (と-base, 'or-else' warning) ↔
  でなければ (ば-base, neutral) ↔ でなくては (ては-base, 'must be', → でなくてはいけない) ↔ でなかったら (たら-
  base) — each pinned to its conditional base + mutually differentiated; のなら (explanatory なら); できれば
  (set 'if possible', ↔ ばいい); でよければ (humble offer); がなければ (negative ば of ある, 'without', ↔
  でなければ identity-vs-existence); ばいい (suggestion, ↔ たらどう & ば〜のに); ば〜ほど (proportional); ば〜のに
  (counterfactual regret, ↔ のに). Anchored to enriched ば/たら/なら/と-conditional/なければ-obligation/ほど/のに.
  Dense webs: ところ-phase timeline, 五段/一段 causative-passive grid, られる homograph disambiguation,
  見える/見られる confusion, reported-belief saying/rule/reasoning trio, negative-conditional と/ば/ては/たら
  base grid. · **batch 15** (だけ/ばかり limitation + 以外/ほか exclusion, 15 indexed + 5 noindex
  redirects): bakari (2-sense only/nothing-but ↔ approximate-amount, anchor)・dake-da・dake-de↔dake-demo↔
  dake-wa・dake-shika(↔shika)・sore-dake・te-bakari-iru・bakari-de(↔dake-de positive/negative);
  the **"not only but also" canonical pair** だけでなく ↔ ばかりでなく (everyday vs literary, mutually
  contrasted) with 4 numbered near-dups (dake-de-wa-naku-2, bakari-de-wa-naku/-2/-4) collapsed to
  **noindex redirect-hubs** → their canonical; igai (以外)↔hoka(ほか)↔hoka-ni-mo, **以外/意外 same-reading
  trap** igai↔igai-to disambiguated; igai-wa → igai redirect. · **batch 16** (person/address suffixes,
  7): honorific ちゃん↔君↔様 (laddered against enriched san) + plural たち↔ら↔方(sonkeigo, elevates)↔
  ども(humbles/derogates) — politeness-direction grid. Fixed kun's truncated seed title ("for pee"→full).
  · **batch 17** (change-of-state する/なる + sensation がする + emotion-display, 8): transformation
  くする(make, transitive ↔ くなる)↔化する(-ize, formal noun-suffix)↔となる(formal become, ↔になる)
  anchored to naru/ni-naru/ni-suru; sensation がする(non-visual perception, restriction vs 見える)↔
  ような気がする(mental hunch, ↔ようだ)↔が気になる(preoccupation, +気にする/気になる note); emotion-display
  がる↔たがる (3rd-person feeling/desire, restriction vs own feeling, anchored hoshii/tai). · **batch 18**
  (する-based inference/condition connectives, 7): すると(2-sense thereupon/in-that-case)↔そうすると;
  とする(set premise, ≠volitional うとする)→とすると(assume-that, +とすれば/としたら variants)↔からすると
  (judging-from, ↔からみると)↔そうすると; となると(when-it-comes-to, topical/hypothetical)↔になると(literal
  time/stage change) — both off enriched となる; anchored to と-conditional/なら/tara/ば.
  · **batch 19** (standpoint/means particles + occasion, 7 indexed + 3 noindex redirects): standpoint
  に関して(formal vs について)↔に関する(adnominal); the by/source/depends triad による(2-sense due-to/
  depends-on)↔によって(3-sense means/passive-agent/varies-by, ↔rareru-2 formal passive agent)↔によると
  (according-to, pairs with そうだ hearsay); occasion 際に(formal 'when', ↔とき/場合)↔最中に(peak-of-action,
  interrupted, ↔間に/ところ). Redirects: については→ni-tsuite, 場合は & の場合は→baai (both attachment
  patterns of enriched 場合).
  · **batch 20** (reason/purpose connectors + grounds/standpoint, 7): ためだ (2-sense reason 'it's
  because'/purpose 'it's for', ↔からだ/わけだ/tame-ni) ; そのため (result 'therefore') ↔ そのために (purpose
  'to that end') — the に flips result→purpose; 以上は (now-that/since, obligation logic, ↔ので/以上に);
  以上に (more-than, ↔より) — 以上 homograph は/に disambiguated; 上で〔うえで〕(2-sense after-deliberation /
  in-doing, ↔てから) ↔ 上〔じょう〕(in-terms-of standpoint) — **上 reading-homograph うえで vs じょう** taught.
  · **batch 21** (こと-reason connectives + 〜までもない idiom + を通して, 5 indexed + 1 redirect): the
  grounds-contrast pair ことから (infer from an observed *fact*) ↔ ことだから (predict from a known
  *character*); the 言うまでもない idiom indexed as the frozen instance of productive 〜までもない ('no need to
  even ~', ↔必要はない nuance) — は言うまでもない folded to a redirect; を通して (2-sense via/throughout,
  +を通じて variant, ↔によって means / として role) — fixed its dangling `o-tsujite` prereq → `o`.
  · **batch 22** (verb completion + capacity/possibility modality web, 7): 切る(complete/utterly)↔切れない
  (can't-finish/too-many)↔かける(begun-unfinished/on-the-verge) — completion arc; 得る(える/うる formal
  abstract possibility, ↔れる concrete ability)↔得ない(あり得ない impossible); the **classic trap pair**
  かねる(polite 'cannot do', keigo decline)↔かねない('might (regrettably) do', undesirable-only, ↔かもしれ
  ない neutral) — same root, opposite polarity, taught explicitly. All off masu-stem. Fixed kaneru's
  truncated seed title.
  · **batch 23** (-ish/tendency/excess suffixes, 4): 気味(slight onset of an unwelcome state, *now*)↔
  がち(recurring tendency *over time*, negative-leaning; enriched ahead of band as the 気味 sibling)↔
  っぽい(2-sense resembles / prone-to, ↔らしい positive 'befitting')↔だらけ(literal heavy excess, negative);
  the four mutually contrasted on degree×time×literal-vs-quality axes.
  · **batch 24** (concessive 〜ても emphasis + permission/futility, 7): the no-matter-how trio どんなに〜ても
  (degree)↔いくら〜ても(quantity/effort)↔たとえ〜ても(hypothetical 'even if'); どうしても (2-sense at-any-cost /
  with-neg just-can't); permission てもかまわない(↔てもいい) vs futility ても始まらない (same ても, opposite
  stance); ても〜なくても (whether-or-not binary). All off enriched te-mo/te-mo-ii.
  · **batch 25** (sentence-final modal particles: wondering / agreement / rhetorical confirmation, 9):
  the **wondering pair** かな (light casual musing, +negative=wish) ↔ かしら (feminine equiv); na-2
  (sentence-final な emotion/agreement, **prohibitive な disambiguated**) ↔ なあ (drawn-out emotional
  variant) — both laddered against enriched ね/よ; よね (よ-assert + ね-confirm, 'right?'); the
  **rhetorical 'isn't it?' register pair** じゃないか (casual contraction) ↔ ではないか (formal full
  form, +volitional 'let us ~'); のだろうか (heavy introspective 'I wonder', ↔かな light vs だろう
  conjecture); だろ (clipped casual だろう→'right?', ↔だろう/でしょう register). Anchored to enriched
  ne/yo/darou/deshou/kamoshirenai/no-2/no-da.
  · **batch 26** (hypothetical-outcome evaluation: suggestion / hope / regret / relief, 6): the
  **suggestion register pair** たらどう (casual 'why don't you') ↔ たらどうですか (polite) — both flagged as
  potentially pushy/unsolicited; the **direction-flip pair** たらどうですか (*gives* advice) ↔ たらいいですか
  (question-word + たらいい, *asks* 'what should I ~?'); といい ('I hope ~', outcome you don't control, ↔
  ばいい advice you do); the **hindsight valence pair** ばよかった (regret 'should have', +なければよかった
  'shouldn't have') ↔ てよかった (relief 'glad I did', +なくてよかった 'glad I didn't'). Anchored to enriched
  ba-ii/tara/hou-ga-ii/te-mo-ii.
  · **batch 27** (listing / enumeration particles, 7): the **exhaustive-vs-representative axis** や
  (noun list 'among others', ↔ と exhaustive) ↔ とか (casual/vaguer, also actions+quotes+single-item
  hedge, ↔ toka-2 hearsay sense) ↔ とかとか (explicit example list); など (2-sense: 'and so on' / belittling
  〜なんか・なんて, pairs with や to close a list); the **clause-listing reasons pair** し ('and what's more',
  cumulative grounds, ↔ から one direct cause) ↔ しし (explicit multi-reason); もも ('both A and B' / with
  neg 'neither nor', ↔ と neutral & も 'also', particle-stacking にも/とも note). Anchored to enriched
  to-2/ka/mo/kara/toka-2. **Slug trap:** reason から is `kara` (not `kara-2` — caught pre-build).
  · **batch 28** (interrogative + でも/も indefinites, 6): the **affirmative-vs-negative sweep pair**
  何でも (anything, question-word+でも free-choice family 誰でも/どこでも/いつでも) ↔ 何も〜ない (nothing,
  question-word+も+neg); いつ(で)も (2-sense: いつでも 'any time' free-choice vs いつも 'always' frequency —
  the で is the difference); いくら reworked to lead with the **'how much?' question word** (concessive
  deferred to the pre-existing enriched いくら〜ても `ikura-temo`, no dup) ↔ いくら〜でも (2-sense:
  でも-allomorph concessive vs fused いくらでも 'any amount'); でも〜でも ('whether A or B', ↔ も〜も
  'both/neither' & de-mo). Anchored to enriched de-mo/mo/te-mo/donna-ni-temo/ikura-temo.
  **Dedup note:** bare adverbs (`ikura`, `donnani`) overlap their enriched 〜ても constructions
  (`ikura-temo`, `donna-ni-temo`) — give the bare node its own non-concessive core + cross-ref, don't
  re-teach the concessive. `donnani` left a stub (donna-ni-temo owns the concessive).
  · **batch 29** (temporal span connectives, 6): 前 (noun, 2-sense space 'front' / time 'ago', ↔前に
  connective which mae-ni owns); 前から ('from before / for a while now', starting-point, ↔前 point &
  kara-3 'from'); the **核 contrast** 間に ('during, at a point within a span'; the に = point vs bare
  間 = throughout) ↔ うちに (2-sense: 'while the chance lasts / before it changes' + ているうちに gradual
  change — adds urgency 間に lacks) — plus ているあいだに (the ている-attachment variant, cross-ref 間に, ↔
  ながら same-subject simultaneity); 間 (かん duration suffix 三時間, reading-split from あいだ connective).
  Anchored to enriched mae-ni/ato-de/nagara/made-ni/te-iru. **Slug trap:** 'from' から is `kara-3`
  (kara=reason). **Dedup:** three 間に faces (aida-ni core / te-iru-aida-ni variant / no-aida-ni left stub);
  前 noun vs mae-ni connective split like ikura/ikura-temo.
  · **batch 30** (comparison & superlative constructions, 5): 方〔ほう〕 scoped to the 'the ~ one / side'
  selection sense (its low-conf ambiguity resolved — のほうが `no-hou-ga` owns comparison, ほうがいい owns
  advice); the **two-way vs many-way axis** と〜と、どちらが (compare exactly 2, ↔ answer のほうが) ↔
  の中で〜が一番 (superlative of 3+, ↔ ichiban); の中で ('among / of all', sets the group, ↔ で scope when
  noun is already whole range, ↔ から for picking-out); ほど〜ない ('not as ~ as', negative-only, ↔ より
  positive comparison). Anchored to enriched no-hou-ga/yori/ichiban/hodo/hou-ga-ii/de.
  **Slug trap:** scope で is `de` (not `de-4`); 'from' = kara-3. Bumped hou-ga conf low→med (scoping
  resolved the role ambiguity).
  · **batch 31** (て-form social/emotional formulas, 3): てね (soft request/reminder, ↔てください plainer
  & ne agreement-softening; てよ pushier sibling noted, conf med→high); the **gratitude-vs-apology pair**
  てくれてありがとう (thanks for a favour, くれて = done-for-me, ↔ kureru) ↔ てすみません (2-sense: apology
  'sorry for ~ing' + すみません-as-thanks 'thanks for the trouble'; なくて negative cause; 〜て申し訳ない
  formal). Anchored to enriched te-form/te-kudasai/kureru/ne. **Milestone: 500 indexed.**
  · **batch 32** (に比べて comparison + と同じ equivalence, 4; extends batch-30 comparison web): the
  baseline-comparison near-pair に比べて (plain 'compared to', ↔ より which ranks head-to-head) ↔ に比べると
  (と-conditional 'when one compares', slightly more tentative); the equivalence pair と同じで (identical
  *in kind*, で=copula て-form, ↔ と違って antonym) ↔ と同じくらい (equal *in degree* 'as ~ as', positive
  mirror of ほど〜ない). Anchored to enriched yori/hodo-nai/no-hou-ga/gurai/to-2.
  · **batch 33** (なんか/なんて/なんと colloquial family, 5; follow-on to batch-27 など): なんか (2-sense
  casual など: example-cite + belittling, ↔ 何か indefinite trap noted); the **なんて homograph pair** なんて
  citing (re-quotes a clause with attitude, = などと contracted, ↔ nanka noun-only) vs なんて-2 exclamatory
  ('how ~!', heads an adjective forward); なんと (2-sense: 'how ~!' formal exclamation + 'believe it or not'
  surprise-flag, ↔ なんて-2 register, ↔ nan-to-ka 'somehow' trap); などと (cite speech/thought dismissively,
  = なんて's full form, ↔ to-quotative neutral). Anchored to enriched nado/toka/to-quotative.
  **Slug trap:** 'somehow' = `nan-to-ka` (not `nanto-ka`).
  · **batch 34** (cause/reason connectives with valence, 5): the **canonical valence-contrast pair** せい
  (noun 'the fault of', negative blame, のせいだ/のせいか/せいにする) ↔ おかげ (noun 'thanks to', positive
  credit, のおかげだ/おかげさまで); their connective forms せいで ('because of ~, bad result', ↔ neutral
  から/ので) ↔ おかげで ('thanks to ~, good result') — same structure, opposite valence; なぜなら (formal
  sentence-opener 'the reason is', pairs with closing からだ, ↔ から embedded & だから result-first).
  Anchored to enriched kara/node/dakara/tame-da. **New QA trap folded into §4/§7:** a Cyrillic word
  (благодаря) slipped into okage.md prose — post-batch scan now covers Cyrillic (Ѐ-ӿ) alongside Hangul.
  · **batch 35** (as-soon-as / the-instant temporal set, 3 indexed + 1 noindex variant): たとたん (the
  instant ~; past + often *unexpected*; bars commands/plans, ↔なり literary) vs the **base-flip pair**
  たらすぐ (たら base → planned/one-off, freely takes requests, ↔たとたん) ↔ とすぐに (と base → automatic/
  habitual, bars commands, ↔to-conditional); たらすぐに kept **noindex** as a trivial に-variant of たらすぐ
  (avoid dup-content tax — same redirect-hub treatment). Anchored to enriched nari/tara/to-conditional/
  ya-ina-ya/sugu. Fixed to-sugu-ni prereq suru-to→to-conditional (とすぐに uses と-result, not すると).
  **Trap caught (×2, batch 13):** Hangul slipped into kana examples — 약束→約束 (rarenai), 체조子→調子
  (no-2) — both fixed pre-build; a post-batch Hangul scan (가-힣 + Jamo) is now mandatory QA. **Extended
  batch 34:** also scan Cyrillic (Ѐ-ӿ) — a stray благодаря slipped into okage.md prose. Combined regex:
  `[가-힣ᄀ-ᇿ㄰-㆏Ѐ-ӿ]`.
  · **batch 36** (に対して contrast/proportional + result + というと/といえば "speaking of" + concessive
  からといって web, 19 indexed + 4 noindex redirects): **に対して** (2-sense: target 'toward' ↔ contrastive
  'whereas', 〜のに対して clause form; に対する adnominal folded to redirect ni-taishite-2) ↔ について (about
  vs toward) ↔ 反面 (two sides of *same* thing, ↔ ippou-de); **につれて** (proportional gradual change, ↔
  にしたがって & ば〜ほど; restriction: no command/one-time event); result pair **その結果** (standalone
  connective, ↔ そのため) ↔ **結果** (bound V-た/Nの結果); the **"speaking of" topic-shift family**: といえば
  (free association) ↔ というと (2-sense: association + confirmation 'so that means?') ↔ といったら (2-sense:
  topic + emphatic 'the sheer ~!') ↔ そういえば (sudden recall, changes subject); the **standpoint pair**
  から言うと (conclusion from a basis, ↔ からすると inference) ↔ で言うと (measure/axis rephrase); the
  **concessive 〜といって web**: といっても (concede-then-qualify, canonical; **といって-mo kana spelling folded
  to redirect to-itte-mo**) ↔ からといって ('just because ~, not necessarily', restriction: main clause
  denial) ↔ だからといって (standalone opener of same logic) ↔ かといって (rejects the *opposite* alternative)
  ↔ といって (med-conf: stated-reason/pretext + これといって idiom); the **かというと set**: かというた→かというと
  (Q-then-answer) ↔ なぜかというと (fixed 'the reason is ~からだ', ↔ なぜなら formal; なぜかというと〜からだ folded
  to redirect) ; どちらかと言えば ('if anything', softening hedge; **と-base どちらかと言うと folded to redirect**).
  Anchored to enriched ni-tsuite/ippou-de/ni-shitagatte/ba-hodo/sono-tame/to-iu/to-naru-to/kara-suru-to/
  nazenara. **Slug traps:** なぜなら = `nazenara` (not naze-nara); 反面 contrast = `ippou-de`. **Redirect-hubs
  (stay noindex):** ni-taishite-2, to-itte-mo, naze-ka-to-iu-to-kara-da, dochira-ka-to-iu-to. **Over-fill
  caught:** dropped a manufactured に対して contrast on どちらかと言えば (no learner confuses them).
  · **batch 37** (さえ emphasis/if-only + たって colloquial concessive + 限り as-long-as + instead-of/
  despite connectives, 9 indexed + 3 noindex redirects): the **さえ family** さえ ('even', extreme example,
  ↔ も plainer) ↔ でさえ (さえ on a subject noun) ↔ さえ〜ば ('if only', the one sufficient condition, ↔ ば
  general); the **たって colloquial concessive pair** たって (た-form + って = casual 〜ても 'even if', ↔ te-mo)
  ↔ たって-2 (**volitional + たって** = 'even if one tries to', futile-effort — a genuine separate construction,
  NOT a dup) ; 限り (2-sense: 'as long as' condition / 'as far as' extent + ない限り 'unless' note, ↔ 間に
  time-span; **限りは folded to redirect**); the **instead-of/despite set** 代わりに (2-sense substitute /
  trade-off-in-exchange, ↔ 反面; **の代わりに folded to redirect**) ↔ くせに ('even though' WITH reproach,
  same-subject restriction, ↔ のに neutral) ↔ 割には ('considering ~', proportional-expectation mismatch,
  ↔ のに/くせに). **を通じて folded to redirect → を通して** (o-toshite, batch-21 enriched). Anchored to
  enriched mo/te-mo/ba/aida-ni/noni/hanmen/o-toshite. **Redirect-hubs (stay noindex):** kagiri-wa,
  no-kawari-ni, o-tsujite. **Fold check that flipped:** tatte-2 looked like a kana dup of tatte but its
  prereq volitional-form revealed the distinct 〜（よ）うたって construction → kept indexed.
  · **batch 38** (degree / frequency / manner adverbials, 8 indexed, no folds): どんなに (scoped to the
  non-concessive 'how (much) ~' exclamation/embedded-Q core; どんなに〜ても concessive stays donna-ni-temo —
  same bare-vs-〜ても split as batch 28's ikura/donnani) ↔ donna-ni-temo; あまりにも ('far too', emphatic
  excess, ↔ amari plain); ちゃんと ('properly', casual of きちんと note); ごとに ('each/every', ↔ おきに gap-
  counting & たびに 'each time'); ぶりに ('first time in', 久しぶり note); 一度に ('all at once', いっぺんに
  note); 再び ('again', formal/written ↔ また everyday); どうか (med, scoped to earnest-plea 'please' ↔
  どうぞ offer; the 'somehow/whether' sense deferred). Anchored to enriched donna-ni-temo/amari/oki-ni/
  tabi-ni/mata/douzo. Flat single-sense adverbs — contrasts only where a real confusable enriched sibling
  exists (chanto/buri-ni/ichido-ni left contrast-empty by design, §1 presence-earned).
  · **batch 39** (だって homograph + では/でも contrastive-particle cluster, 5 indexed): the **だって homograph
  pair** だって (sentence-initial 'because', casual/defensive ↔ から neutral; pairs with 〜もん) vs だって-2
  (particle 'even', N+だって ↔ でも casual equiv) — mutually disambiguated; でもある (parse-trap: で+も+ある
  'is also', additional truth, ↔ でも 'even/but'; 〜でもあり〜でもある frame); では (contrastive topic, で role +
  は; ↔ で neutral & は direct-topic; sentence-initial では='well then' noted); ではなくて ('not A but B'
  correction, ↔ janai plain negation; じゃなくて casual). Anchored to enriched kara/de-mo/de/janai (+ wa
  stub). **Slug note:** では = `de-wa` (dewa MISSING is fine); じゃない = `janai` (ja-nai MISSING).
  · **batch 40** (まま state set, 1 indexed + 1 redirect): まま 2-sense ('while left in a state' V-た+まま,
  た-form required — restriction; vs 'as it is/unchanged' そのまま・Nのまま) ↔ ている (unchanged-with-neglect
  vs plain progressive) & ないで (ないまま lingering-undone state); **ままで folded to redirect → mama** (まま+で,
  で usually droppable). Anchored to enriched te-iru/nai-de.
  · **batch 41** (ずつ distributive, 1 indexed): ずつ ('~ each / at a time', equal amount per unit/step) ↔
  ごとに (unit-focus 'every X' vs ずつ amount-focus). Single node done at context-budget tail. Anchored goto-ni.
  · **batch 42** (simile/'as if' modality + ところ connectives, 7 indexed + 1 redirect): **simile set** —
  のような (adnominal 'like ~', modifies a NOUN ↔ youda predicate / youni adverbial; のように・みたいな variants) ↔
  まるで〜ようだ (vivid 'just like', +neg='completely not' note) ↔ かのようだ (formal/written 'as if', explicitly
  counter-to-fact; often まるで〜かのようだ). mitaida was ALREADY a redirect-hub → mitai (left as-is). **ところ
  connectives** — ところで (2-sense: 'by the way' topic-shift / V-た+ところで futile 'even if', ↔ ところが) ↔
  ところが ('however', SURPRISING actual result ↔ しかし neutral) ↔ ところに/へ ('right when', interruption at
  the exact moment ↔ 間に span / たところ completion) ↔ ところだった ('was about to / almost', counterfactual
  near-miss ↔ るところだ real imminence; pairs もう少しで/危うく). **ところだ folded to redirect → ru-tokoro-da**
  (batch-12 aspect trio owns the 3-phase). Anchored to enriched youda/youni/mitai/shikashi/aida-ni/ta-tokoro/
  ru-tokoro-da. **Overlap caught:** mitaida & tokoro-da both already covered by enriched siblings → redirect,
  not re-teach.
  · **batch 43** (intention / projection / pretense modality, 6 indexed): 予定だ (fixed arranged schedule,
  external/objective ↔ つもり personal will); the **つもり family** つもりで ('with the intention/mindset',
  adverbial frame ↔ plain つもり predicate) ↔ つもりだった ('had intended but didn't' + V-た 'thought I had ~'
  self-correction); ふりをする ('pretend', intentional act ↔ かのようだ observer-simile — cross-link to batch
  42); the **ように+verb projection pair** ように祈る ('pray/hope that', uncontrollable outcome ↔ youni purpose;
  verb usually potential/intransitive) ↔ ように〜てほしい (med, 'want you to ~ so that ~', purpose-clause +
  てほしい ↔ bare te-hoshii). Anchored to enriched tsumori/youni/hoshii/te-hoshii/ka-no-you-da.
  · **batch 44** (difficulty suffixes + span-range particles + compound-verb aspect set, 10 indexed):
  the **difficulty pair** にくい (everyday physical/practical 'hard to', ↔ enriched やすい exact opposite,
  i-adj conjugation) ↔ 難い〔がたい〕(literary, psychological/abstract, limited verb set 信じ難い/忘れ難い,
  ↔ にくい register+scope, ↔ かねる polite-decline); the **span-range frame** にかけて (vague far edge of a
  range, ↔ まで precise endpoint; にかけては 'when it comes to' idiom noted) ↔ から〜にかけて (two fuzzy
  edges, ↔ から〜まで exact boundaries); the **compound-verb aspect set** 上がる・上げる (finish to a
  produced result, intransitive/transitive pair, ↔ 切る exhaust-quantity ↔ 終わる neutral-stop) · 合う
  (reciprocal 'to each other', plural-subject restriction, ↔ 続ける; お互いに note; vs standalone 合う 'fit')
  · 込む (**2-sense**: ①inward 乗り込む/詰め込む ②thoroughly 考え込む/話し込む, ↔ 切る) · 直す (redo-to-correct,
  first-try-flawed restriction, vs もう一度 neutral repeat, vs standalone 直す 'repair') · 通す (sustain one
  stance to the end 押し通す/守り通す, ↔ 抜く hardship vs ↔ 切る complete) · 抜く (push through *hardship* to
  the end 耐え抜く/生き抜く, ↔ 通す consistency vs ↔ 切る neutral; vs standalone 抜く 'extract'/手を抜く idiom).
  Anchored to enriched yasui/kaneru/made/kara-3/kiru/owaru/tsuzukeru. **Missing anchors handled as prose
  notes** (tagai-ni, deru, uru absent — お互いに/standalone-verb caveats went to `notes`, not `contrasts`).
  · **batch 45** (temporal after/since/before/during + もの/もん modality + conjecture/likelihood
  modality, 15 indexed): **temporal set** — the **near-synonym pair** 以後〔いご〕(boundary 'from then on';
  also standalone adverb 'henceforth' with corrective tone) ↔ 以降〔いこう〕(range marker, needs a stated
  time anchor, can't float as 'henceforth') ↔ 以来〔いらい〕(looks back from a past point *to the present*,
  continuous; ↔ kara-3 plain 'from'); ないうちに ('before an unwanted change', urgency ↔ 前に neutral; ↔
  うちに affirmative 'while favourable state lasts' — same window, opposite side); 中〔ちゅう〕(に) (**2-sense**
  ①in-the-middle 会議中 ②within-a-period 今日中に; **じゅう reading = 'throughout' 一日中** noted, ↔ aida-ni
  noun-bound vs clause, ↔ made-ni hard deadline); の間に (Nの attachment variant of 間に; に=point→one-time
  main clause, ↔ aida-ni / te-iru-aida-ni forms). **もの modality** — ものだ (**2-sense** ①general-truth
  赤ちゃんはよく泣くものだ ②social-norm 'should' 約束は守るものだ + ものではない 'shouldn't'; exclamatory +
  たものだ note; ↔ beki-da specific-act vs general-norm, ↔ hazu-da deduction vs norm) ↔ たものだ ('used to',
  nostalgic past habit ↔ ていた neutral) ↔ もん (casual sentence-final もの, self-justifying excuse, pairs
  だって〜もん; ↔ から neutral, ↔ datte front-of-sentence). **Conjecture/likelihood certainty-scale** —
  に違いない (firm conviction 'must be', ↔ hazu-da deduction, ↔ kamoshirenai low end, ↔ darou softer) ↔
  考えられない (firm rejection 'unthinkable', opposite pole; ↔ enai impossible); だろうか ('I wonder',
  assertion→doubt via か, ↔ darou assert, ↔ kana casual); 可能性がある (objective gradable probability, ↔
  kamoshirenai subjective, ↔ osore-ga-aru risk-only negative); 〜そうにない (negative appearance そう 'unlikely',
  ます-stem, ↔ souda-2 positive) ↔ そうになる ('almost/near-miss', usually past, involuntary; ↔ tokoro-datta
  circumstance vs ↔ kakeru actually-begun). **Prereq fix:** sou-ni-nai seed prereq souda→**souda-2**
  (appearance そう, NOT hearsay そうだ); sou-ni-naru += souda-2. **Confidence bumps:** igo/ikou/chu-ni
  med→high (meanings standard/solid, cleared the gate). Anchored to enriched ato-de/mae-ni/aida-ni/
  te-iru-aida-ni/made-ni/kara-3/uchi-ni/mono/beki-da/hazu-da/te-ita/kara/datte/kamoshirenai/darou/kana/
  osore-ga-aru/souda-2/tokoro-datta/kakeru/enai. **Homograph trap navigated:** souda (hearsay) vs souda-2
  (appearance 'looks like') — the sou-ni-* nodes belong to souda-2.
  · **batch 46** (can't-help/unbearable emotion-intensity + から standpoint/judging-from + から reason-emphasis
  + only/limitation, 17 indexed): **can't-help family** — たまらない (standalone 'can't stand it', +positive
  'irresistible' note) ↔ てたまらない (sharp/physical intensity) ↔ てしかたがない (everyday 'can't help feeling',
  てしょうがない casual variant) ↔ てならない (literary, feelings/impressions only); 仕方がない ('it can't be
  helped' resignation, vs てしかたがない 'can't help feeling' — same chars opposite function; ↔ shika-nai
  action); ならない (**disambiguation hub**: spontaneous-feeling てならない vs obligation なくては/ねば+ならない —
  taught as element-recogniser, ↔ te-naranai/nakereba-naranai). **から standpoint/judging-from family**
  (the と/て/して/言って quartet, all off enriched kara-suru-to/kara-iu-to): から見て (cite basis) ↔ から見ると
  (foreground viewpoint-shift, て-vs-と form) ↔ からして ('even from just X', single representative + 'to say
  nothing of rest' sense) ↔ から言って (apply a standard/criterion, ↔ から言うと). **から reason-emphasis** —
  からこそ ('precisely because', emphatic+のだ, ↔ kara/node) ↔ からには ('now that/since', resolve/obligation
  main clause, ↔ ijou-wa near-syn) ↔ からだ (sentence-final reason, pairs なぜなら, ↔ kara embedded/wake-da
  realization). **only/limitation** — しかない (**2-sense** no-choice V-る+しかない / 'only' N+しか+ない, ↔
  yori-hoka-nai formal) ↔ でしかない ('merely/nothing more than', dismissive, ↔ ni-suginai measured/shika
  count-vs-value) ↔ きり (**2-sense** 'only' 二人きり / V-た+きり 'and then nothing' 寝たきり, ↔ dake neutral/shika
  needs-neg) ↔ たった ('a mere', emphasises small NUMBER only, ↔ dake/wazuka). **Confidence bumps:**
  shikata-ga-nai low→high (clear common phrase), kara-shite med→high. **naranai** kept med w/ review_reason
  (bound-element hub). Anchored to enriched kara/kara-3/kara-suru-to/kara-iu-to/node/wake-da/nazenara/ijou-wa/
  shika/dake/wazuka/ni-suginai/yori-hoka-nai/nakereba-naranai/te-ita. **Note:** te-shou-ga-nai (てしょうがない)
  remains a noindex stub — folded as a *variant note* on te-shikata-ga-nai, candidate redirect later.
  · **batch 47** (向け/向き suitability-vs-intent pair, 2 indexed; small tail batch near context ceiling):
  向け ('deliberately made/aimed FOR a target', maker's intent) ↔ 向き (**2-sense**: 'naturally suited to' +
  literal 'facing'; 前向き/後ろ向き idiom note) — the classic confusable pair taught on the intent-vs-suitability
  axis. Both off no enriched sibling (self-contained pair). Next obvious tight pairs in the band: muke/muki
  done → 自分/自身 (jibun/jishin self), もしも〜なら/もしも〜たら (moshimo conditionals).
  · **batch 48** (自分/自身 reflexive pair, 2 indexed; tail batch): 自分 (standalone reflexive pronoun
  'oneself', subject-bound; humble-'I' note) ↔ 自身 (emphatic suffix on a noun/pronoun 'that very ~';
  combine: 自分自身) — standalone-pronoun vs bound-emphatic-suffix axis. Both bumped med→high (meanings
  solid). Self-contained pair. Next tight pair: もしも〜なら/もしも〜たら (moshimo conditionals).
  · **batch 49** (N5 high-priority basics: が-predicates + basic verbs + means/or/agent particles +
  interjection, 10 indexed): the **が-marking skill/preference predicates** — のが上手 ↔ のが下手 (mutual
  good/bad-at-an-activity pair, Vる+のが+な-adj; 上手 boastful-of-self note → 得意, 下手 vs 苦手 note) ;
  好きだ (な-adj fondness, **object takes が not を** restriction ↔ 欲しい want-to-obtain, both が; 大好き/
  嫌い/のこと notes) ; 要る (to-need, **u-verb despite -る** + が-object restriction ↔ 必要がある formal/
  abstract+actions) ; 知る (**punctual-verb asymmetry** 知っている 'know' / 知らない 'don't know' — the
  classic trap ↔ ている resulting-state; 知る vs 分かる note) ; particles — か-2 ('or', noun-list; added
  examples, was partially seeded ↔ ka full particle) · に-4 (passive/receiving agent 'by/from'; **created-
  thing agent → によって not に** restriction ↔ から source/giver, organizations prefer から) ; を使って
  (means 'using', て-form of 使う ↔ で plain instrumental, によって formal) ; どうぞ (offer/invite/grant
  interjection ↔ どうか earnest plea; どうも 'thanks/somehow' confusion note). **Confidence bumps:** iru-4/
  sukunai low→high, shiru/sukida/o-tsukatte med→high (meanings standard N5 vocab, gate cleared). Fixed
  sukida's truncated seed title (unbalanced paren). Anchored to enriched no-ga-heta/no-ga-jouzu/hoshii/
  hitsuyou-ga-aru/te-iru/ka/kara-3/rareru-2/de/dou-ka. **Slug note:** に agent = `ni-4`, 'or' = `ka-2`,
  'from' = `kara-3`.
  · **batch 50** (N4 material/particle/conditional basics, 9 indexed): the **material-origin pair** でできる
  ('made of', material still visibly itself, ている-state ↔ から作る) ↔ から作る ('made from', raw material
  transformed beyond recognition; fixed truncated seed title) — the で/から visible-vs-transformed split;
  the **を intransitive-verb pair** を-2 (path/space traversed 道を歩く, motion-verb-only restriction ↔ で
  location of action) ↔ を-3 (departure/separation 家を出る・電車を降りる, 卒業 takes を not から ↔ を-2 through-vs-
  away, ↔ から-3 leaving-act vs starting-point) — both off enriched を object; も-2 ('even', extreme example;
  number+も+neg='not even', +affirm='as many as' restriction ↔ さえ stronger conditional-push, ↔ も additive
  'also'); なくても ('even if not', negative of ても ↔ te-mo; 〜なくてもいい 'don't have to' set-phrase note);
  か〜か ('whether or', brackets 2 alternatives ↔ か〜ないか yes/no on one action, ↔ か-2 plain 'or';
  embedded-Q under 分からない/決める note); もし(も) ('if' adverb — **only signals, doesn't form, the
  conditional** restriction ↔ たら; もしも emphatic note); 少なくない ('not few' litotes ↔ 少ない, 少なからず
  formal note — follows batch-49 sukunai). Anchored to enriched de/o/mo/sae/te-mo/ka-2/ka-nai-ka/tara/
  kara-3/sukunai/nakute. **Slug note:** を path = `o-2`, を departure = `o-3`, も 'even' = `mo-2`.
  · **batch 51** (N4 remainder — evaluation/polite + form-reference + affix/ordinal + connective/notice
  grab-bag, 12 indexed; **drains the N4 common band**): いい (core い-adj — **irregular よ-stem** restriction
  past よかった/neg よくない/adv よく; 良い formal + 「いいです」declining-tone note) ; いかが (polite teineigo
  ↔ どう register pair; いかがでしょうか note) ; **命令形** (imperative reference page — godan -u→-e / ichidan
  +ろ / しろ・せよ / 来い; rough male-only usageSetting ↔ てください polite / なさい softer; せよ literary note) ;
  **自動詞・他動詞** (intransitive-vs-transitive reference — が-undergoes vs を-acts-on restriction, ×ドアを開く ↔
  てある deliberate-state; pairs 開く/開ける best learned together) ; 真っ〜 (intensifier prefix, **non-productive
  fixed set** + 真ん allomorph restriction) ; 〜目 (ordinal suffix, attaches to a counter, 三人 vs 三人目 ↔ 番目
  note) ; んだけど (softening preface — explanatory んだ + trailing けど ↔ kedo plain-contrast / no-da) ; に気がつく
  (notice, thing-noticed takes に not を restriction ↔ が気になる preoccupation; 気づく synonym) ; おい (rough
  male 'hey!' interjection, usageSetting; おーい long-distance note) ; と一緒に (together-with ↔ to-2 plain 'with',
  emphasis on joint; 一人で opposite) ; 〜は〜の一つだ ('one of the' copula pattern, 〜の一人 for people note) ;
  ところ (**2-sense base nominalizer**: ①moment/juncture ②aspect/part — kept distinct from the enriched
  〜ところだ aspect trio, **routes to ru-tokoro-da + the tokoro-de/-ni/-ga sub-construction pages** rather than
  re-teaching). **Confidence bumps:** ii/jidoushi-tadoushi low→high, me med→high (meanings standard, gate
  cleared). Anchored to enriched dou/te-kudasai/nasai/te-aru/kedo/no-da/ga-ki-ni-naru/to-2/ru-tokoro-da.
  **Overlap navigated:** bare ところ vs the dedicated ところ-construction nodes (12 of them) — taught the
  nominalizer core once + cross-linked, no dup-content. **N4 common band now drained → next is N3 common.**
  · **batch 52** (N3 common opener — もしも conditionals + か whether/or family + こそ/reason set + み/面
  suffixes, 10 indexed): the **もしも conditional pair** もしも〜なら (picks up a premise, main clause can
  precede ↔ もしも〜たら / nara) ↔ もしも〜たら (event-then-result sequence ↔ もしも〜なら / tara) — both off
  batch-50 もし(も); the **whether/or set** か〜ないか ('whether or not', repeat-verb yes/no ↔ か〜か two distinct
  options; 〜かどうか everyday-syn note) · か何か ('or something', single-example hedge, 何=indefinite restriction
  ↔ とか loose-list; 誰か/どこか parallel note) · または (formal/written exclusive 'or' ↔ か-2 spoken; それとも/
  あるいは notes); the **こそ/reason set** こそ ('precisely/exactly', replaces は/が restriction ↔ からこそ reason-
  emphasis; てこそ note) · のだから ('because as-you-know', established reason → assertion/command main clause ↔
  から plain cause; んだから/んだもん notes) · なぜか ('for some reason', cause unknown ↔ なぜなら gives-reason —
  opposite jobs same なぜ; なんだか syn); the **suffix pair** み ('-ness', subjective felt quality, **non-productive
  fixed set** ↔ さ objective measurable+productive — THE pair) · 面 ('in terms of/aspect', facet-to-evaluate ↔ 上
  domain-it-holds-in). **Fixed truncated seed titles:** koso, mi. Anchored to enriched nara/tara/moshi-mo/ka/
  ka-ka/toka/ka-2/kara-koso/kara/dakara/no-da/nazenara/sa/jou. **Slug note:** 'whether-or-not' = `ka-nai-ka`,
  'or something' = `ka-nani-ka`.
  · **batch 53** (N3 common — にしても/にしては standard-vs-concession + prohibition/instruction + こと-connectives
  + 'rather/somehow' adverbs, 8 indexed): the **に+する は/も pair** にしても ('even if/even granting', concession
  ↔ にしては / te-mo; それにしても opener note) ↔ にしては ('for/considering', surprising mismatch vs a **concrete
  known standard** restriction ↔ にしても / 割には wari-ni-wa proportional); the **prohibition pair** 〜な (rough
  'don't!', dictionary-form + stressed, ↔ 命令形 negative-counterpart / na-2 sentence-final disambiguated) ↔
  ないようにしてください (polite 'make sure not to', ongoing-care vs one-off restriction ↔ てはいけない firm-rule /
  〜な rough; affirmative ようにしてください note); the **こと-connectives** ことで ('by ~ing', means-to-result ↔ て
  sequential; のことで 'regarding' / ということで 'so' disambiguated; bumped med→high) · 〜ことは〜が ('admittedly ~
  but', repeat-word grudging concession; 〜には〜が frame note); 'rather/somehow' adverbs むしろ ('rather/if
  anything', completes 〜というより ↔ to-iu-yori) · なんとか ('somehow=manage-to by effort' ↔ batch-52 なぜか
  'somehow=unknown-cause' — the 'somehow' trap; なんとかなる/なんとかさん notes). Anchored to enriched ni-shiro/
  te-mo/wari-ni-wa/imperative/na-2/te-wa-ikenai/koto/te-form/to-iu-yori/naze-ka. **Slug trap caught pre-build:**
  割には = `wari-ni-wa` (not warini). **'somehow' pair split:** なんとか (method) vs なぜか (cause) cross-linked.
  · **batch 54** (N3 common — に-based connectives + 'without' pair, 7 indexed): に当たる ('correspond to/be
  equivalent to'; にあたって 'on occasion of' + literal 'hit' disambig note; med→high) · に合わせて ('adjust-to-
  match', deliberate fitting ↔ にしたがって follow-rule/proportional) · によれば ('according to', pairs hearsay
  ending ↔ によると ni-yoru-to near-identical, formal-vs-spoken) · に慣れる ('get used to', thing takes に not を,
  のに for actions; 慣れている state + 慣らす transitive notes) · に限る ('nothing beats', subjective verdict —
  **disambiguated from 限る 'limit' / に限らず / に限って** ↔ ほうがいい measured-advice); the **'without' pair**
  なしで (noun + 'without' ↔ ないで verb 'without ~ing'; なしでは/なしに/抜きで notes) ↔ なく (formal continuative
  negative of ない, written clause-link ↔ ないで spoken / ずに classical; ことなく/絶え間なく notes; med→high).
  Anchored to enriched ni-shitagatte/ni-yoru-to/ni-yoru/hou-ga-ii/nai-de/zu-ni/nai. **Confidence bumps:**
  ni-ataru/naku med→high.
  · **batch 55** (N3 common — report/obvious/concession/purpose + adverbs, 6 indexed): んだって (casual hearsay
  'I hear' ↔ そうだ neutral/written; rising-intonation = confirm-rumour; って relay note) · 当たり前だ ('only
  natural/obvious', THIS-thing-expected ↔ ものだ general-norm; 当然 formal syn) · ながらも ('although/even while',
  concessive も on ながら, shared-subject+states restriction ↔ ながら 'while' / のに spoken-concessive; 残念ながら/
  我ながら fixed) · には ('in order to' purpose — Vる+には, main clause = need/means/eval restriction ↔ ために
  action-for-purpose; topic-emphasis には noted as separate; med→high) · 一般に ('generally', formal ↔ 普通/たいてい
  speech; 一般的に syn) · なるほど ('I see', acknowledge-understanding; **superior-caution** usageSetting → 勉強に
  なります/おっしゃる通り). Anchored to enriched souda/tte/mono-da/nagara/noni/tame-ni/youni. **Confidence bump:**
  ni-wa med→high.
  · **batch 56** (N3 common — casual sentence-final particles + listing/additive, 5 indexed): だい (casual
  **masculine wh-question** marker ↔ ka neutral / かい yes/no-pair; dated/fictional; fixed truncated title) ·
  っけ ('...was it?/...again?' recall-particle, **takes past だっけ/たっけ even for present** ↔ ka plain-ask;
  muttered-to-self note) · 何〜も ('as many as', 何+counter+も indefinite-large-number ↔ mo-2 三〜も specific;
  **vs 何も+neg 'nothing'** disambig; med→high) · などの ('such ~ as', examples→category head-noun ↔ など
  list-closer; や〜などの frame) · あと ('and also/besides' casual afterthought ↔ それに composed; **disambig
  from 後で 'after' / あと三日 'remaining'** — kana-written additive; med→high). Anchored to enriched ka/mo-2/
  nado/sore-ni. **Confidence bumps:** nan-mo/ato med→high. **Session 49–56: 618 → 685 (+67).**
  · **batch 57** (N3 common tail, 3 indexed): と関係がある ('related to', thing takes と; 関係がない negative /
  関係なく/関係者 notes ↔ に関して topic-intro) · もともとの ('original' adnominal of もともと; bare-adverb もともと
  'originally' + 本来 notes; med→high) · 一方だ ('keeps getting more/worse', one-direction trend, Vる+一方だ ↔
  ていく neutral-change; **disambig from 一方で 'meanwhile' / noun 一方**; med→high). Anchored to enriched
  ni-kanshite/iku. **Confidence bumps:** motomoto-no/ippou-da med→high. **Session 49–57: 618 → 688 (+70).**
  · **batch 58** (N3 common — discourse connectives + modality/question/particle grab-bag, 29
  indexed + 1 redirect): **Cluster 1 — というX定義/言い換え + それ-connectives + openers + temporal/
  degree adverbs (17 + 1 redirect):** というのは (2-sense definition 'X means' / reason, ↔ つまり/
  ということは) ↔ つまり (restate-as-conclusion, ↔ というのは/要するに) ↔ というより (reject first label,
  ↔ むしろ pair / より degree) ↔ という理由で (formal stated grounds, ↔ から) ↔ というふうに (cite a manner,
  ↔ ように); それと (tacked-on extra, ↔ それに reinforcing / そして sequence) ↔ それとも (alt-question 'or',
  ↔ か-2 phrase-level / あるいは formal) ↔ そこで (deliberate action-in-response, ↔ だから/それで; **med→high**);
  さあ (2-sense prompting / hesitation, ↔ さて) ↔ さて (topic-shift, ↔ つまり/そこで); せいぜい (upper-limit
  'at most', ↔ せめて minimum-hope); しばらく ('for a while'; long-gap-greeting note); つい (2-sense
  lapse-vs-self-control / 'just now', ↔ 思わず reflexive / うっかり careless); ついでに (secondary task on
  same errand, ↔ ながら simultaneous); 通りに (exact match to a model, ↔ ように manner / まま unchanged;
  〜どおり fusion); 途中で (midway/on-the-way, ↔ 間に span); 例えば (flat). **totan-ni (途端に) → noindex
  redirect → ta-totan** (batch-35 owns 途端). **Cluster 2 — modality/seeming + softened/rhetorical
  question + particle/difficulty (12):** と言える (warranted conclusion, ↔ だろう conjecture) · とみえる
  (infer from observed evidence, ↔ ようだ everyday / らしい hearsay; **fixed truncated title**) ·
  のでしょうか (polite 'I wonder', ↔ のだろうか plain) · たらいいか (Q-word 'what should I ~?', ↔ ばいい
  states-advice) · 反語 rhetorical-question (reference: question-shape = forceful opposite, ものか/
  だろうか, ↔ だろうか; **fixed truncated title**) · ただ (2-sense 'only/just' / caveat 'however', ↔ だけ
  particle / しかし full-contrast; ただし note; **med→high**) · ときには ('at times', ↔ たまには) ↔ たまには
  ('once in a while / for a change', treat-yourself); てごらん (gentle superior→inferior 'try ~ing',
  ↔ てみる neutral / なさい firmer) · づらい (doer's-discomfort 'hard to', ↔ にくい objective / 難い literary)
  · ぞ (rough masculine forceful-assertion, ↔ よ inform; ぜ note) · ずに (formal 'without ~ing', せずに
  irregular, ↔ ないで spoken / なく formal-link). Anchored to enriched to-iu/tsumari/yousuru-ni/
  to-iu-koto-wa/mushiro/yori/sore-ni/soshite/ka-2/aruiwa/dakara/sore-de/youni/mama/aida-ni/ta-totan/
  darou/youda/rashii/no-darou-ka/ba-ii/darou-ka/dake/shikashi/toki/nikui/gatai/te-miru/nasai/yo/nai-de/
  naku. **Slug traps:** 'or' = `ka-2`; だろうか = `darou-ka`. **Missing-target notes (→ prose, not
  contrasts):** tokidoki, semete (exists), ze, deshou-ka, tara-ii all absent or routed around.
  · **batch 59** (N3 common — として particle family + purpose/projection ように + concession +
  を-connectives + interval/state/reason grab-bag, 21 indexed): **として family** として (role/standpoint
  'as'; として〜ない 'not a single' note) ↔ としては (standpoint/judgment-yardstick 'as for / for a ~', ↔
  にしたら feelings-viewpoint) ↔ としても (**N2** hypothetical 'even if/assuming', ↔ ても basic / にしても
  already-true; **med→high**; distinct from role として+も). **purpose/projection ように** ように言う (indirect
  command 'tell to ~', ↔ と言う direct; **med→high**) · のに-2 (**purpose のに** 'for ~ing', Vる+のに+cost/
  便利, ↔ ために goal; **disambiguated from concessive のに** by dict-form-only attachment; **med→high**) ·
  ようとしない ('won't even try', volitional+としない, ↔ ようとする). **concession** 確かに〜が ('admittedly but',
  self-raised concession; **med→high**) ↔ そうですが (dialogue reply 'that may be so but'; **med→high**) ·
  **は** (contrastive/emphatic advanced は: implicit-contrast + neg-scope-limiting 高くはない + particle-
  stacking には/では, ↔ が subject-focus / も additive; nuance fires; **conf med + review_reason**, broad).
  **を-connectives** を込めて (pour-emotion-into, 心/愛/感謝) · をはじめ(として) (lead with a representative
  example, ↔ など loose-list) · を左右する (decisive influence 'make or break', 左右→swing; **med→high**).
  **interval/state/reason** おきに (gap-interval 'every other', ↔ ごとに inclusive — 一日おきに trap) ·
  っぱなし (**2-sense** neglect-left-as-is / continuously, ↔ てある deliberate) · て済む ('manage with just
  ~ing', ↔ ずに済む 'without having to') · てからでないと ('unless first ~', ↔ てから neutral-order) · ている
  場合じゃない ('no time to be ~ing', ↔ どころではない stronger) · おかげで ('thanks to', positive twin of せいで,
  ↔ から neutral) · まるで (simile-intensifier pairs ようだ, ↔ marude-you-da frame; **+neg='completely not'**)
  · 行う (formal 'carry out', ↔ やる casual; おこなう≠いく + passive 行われる; **low→med**) · 〜的 ('-ic/-al'
  na-adj/adverb suffix, ↔ 風に concrete-style). Anchored to enriched to-shite/youni/you-to-suru/to-iu/
  tame-ni/noni/wa-2/ga-2/mo/tashika-ni/te-mo/ni-shitara/sei-de/kara/nado/goto-ni/te-aru/zu-ni-sumu/te-kara/
  dokoro-de-wa-nai/marude-you-da/fuu-ni/yaru. **Dangling-slug fix:** okonau contrast suru→yaru (**no
  standalone する node exists**; する kept in prose). **Still pending catalog fold decision:** o-suru/
  o-suru-2, yaru/yaru-3/te-yaru (left as stubs).
  · **batch 60** (N2 common opener — という X family + もの modality + emphatic total-negation, 12 indexed
  + 1 redirect): **emphatic negation** 一切〜ない (categorical 'none whatsoever', formal/rules, ↔ まったく
  everyday; +affirm='everything') · ろくに〜ない ('not properly', done-but-inadequately + complaint tone,
  ↔ まったく entirely-not) · なくはない (reluctant double-negative partial-yes, ↔ わけではない denies-conclusion).
  **(sukoshi-mo-nai already a redirect-hub → enriched sukoshi-mo; skipped.)** **という X family** ということは
  (forward inference 'that means', ↔ つまり restate / というのは backward-define) · というか (groping
  self-correction 'or rather / actually', ↔ というより flat-rejection) · とは (**2-sense** formal definition /
  trailing-off surprise 'to think that ~!', ↔ というのは conversational; **med→high**) · というのに (emotional
  'even though', complaint-laden, ↔ のに plain) · というものだ (emphatic verdict 'that's what ~ really is',
  ↔ ものだ general-norm; 〜というものではない denies-overgeneralization). **もの modality** ものの (dry written
  concession 'although, but in fact', ↔ のに emotional / とはいえ whole-point) · ものだから (excuse-giving
  'because, you see', unintended-result, no commands, ↔ から plain / ので objective; もんだから casual) ·
  **ものですから → noindex redirect → mono-dakara** (polite-register variant; fixed truncated title) ·
  ものがある (felt-impression 'there's something ~ about it', subjective-evaluative, ↔ ものだ norm) ·
  ものではない (social-norm 'one shouldn't', common-sense, ↔ べきだ logical/duty). Anchored to enriched
  mattaku/sukoshi-mo/wake-de-wa-nai/tsumari/to-iu-no-wa/to-iu-yori/noni/mono-da/mono/to-wa-ie/kara/node/
  beki-da. **QA catch:** a stray Cyrillic 'ків' slipped into mono-de-wa-nai's reading — caught by the
  mandatory foreign-script scan, fixed pre-build (reinforces: scan is non-optional even on a 1-line field).
  · **batch 61** (N2 common — に-compound families: basis/according-to + regardless/contrary + direction,
  13 indexed + 3 redirects): **basis / according-to** に基づいて (binding foundation/standard, ↔ をもとに
  raw-material) ↔ をもとに(して) (springboard to create from) · に沿って (**2-sense** physical 'along' /
  conformity 'in keeping with', ↔ に従って obey) · に応じて (flexibly vary-with, ↔ に従って / **に応えて same-
  kanji 応 reading trap こたえる vs おうじる**) ↔ に応えて (live-up-to expectations) · に伴って (one change
  accompanying another, single-event ok, ↔ につれて gradual-only / に従って). **regardless / contrary** に反して
  (result violates expectation/rule, ↔ に対して mere-contrast) · **に反する → redirect → ni-hanshite** ·
  **にかかわらず ↔ にもかかわらず — THE も-pair**: にかかわらず (regardless of a variable, result constant) ↔
  にもかかわらず (in-spite-of a fact, surprise) · を問わず (category 'any ~ is fine', ↔ にかかわらず opposite-
  pairs) · に限らず ('not limited to', ↔ だけでなく `dake-de-wa-naku`; disambig に限って/に限る) · **にも関わらず
  → redirect → ni-mo-kakawarazu** (kanji). **direction** に向かって (physical/immediate 'heading toward /
  shouting at', ↔ へ destination) ↔ に向けて (goal/deadline/audience 'aimed at / in prep for') · **に向けて／
  向けた → redirect → ni-mukete** (adnominal). Anchored to enriched ni-shitagatte(stub)/ni-tsurete/
  ni-taishite/e/dake-de-wa-naku/noni. **Slug traps:** だけでなく = `dake-de-wa-naku` (caught at lint); に反する
  = `ni-hanshite-2`. **QA catches (×2):** bogus `attaposed:` formation key in o-moto-ni (removed); duplicate
  ni-mukatte contrast slug in ni-mukete (de-duped → notes). **Redirect-hubs (stay noindex):** ni-hanshite-2,
  nimo-kakawarazu, ni-mukete-muketa.
  · **batch 62** (N2 common — additive 'moreover' connectives + natural/certainty modality, 10 indexed
  + 4 redirects): **additive set** (all same-direction 'on top of that'): に加えて (attaches to NOUN, formal,
  ↔ その上 sentence-connector) · その上 (sentence-connector 'moreover', ↔ しかも / に加えて) · **その上に →
  redirect → sono-ue** · さらに (**2-sense** addition / 'even more' before comparative — the sense その上
  lacks) · しかも (additive + 'and that's not all', striking/extreme, ↔ その上 / さらに) · おまけに (casual
  emphatic, piles-on-misfortune, ↔ その上 formal) · 上に〔うえに〕 (attaches to CLAUSE A上にB, ↔ に加えて noun /
  その上 new-sentence; **disambig from 上で/上〔じょう〕**) · および (formal written 'and' for nouns, forms/
  documents, ↔ と casual). **natural/certainty modality:** 当然だ (canonical 'only natural/of course', ↔
  当たり前だ blunter / はずだ deduction-vs-deserved; **med→high**) ← **て当然だ・も当然だ・のも当然だ all →
  redirect → touzen-da** (attachment-pattern variants) · に決まっている (emotional 'obviously, no question',
  ↔ に違いない reasoned / はずだ measured; **low→high**) · っこない (casual blunt 'no way', ます-stem, ↔ わけ
  がない logical). Anchored to enriched dakara/mata/to-2/atarimae-da/hazu-da/ni-chigainai/wake-ga-nai.
  **Redirect-hubs (stay noindex):** sono-ue-ni, mo-touzen-da, no-mo-touzen-da, te-touzen-da. **Clean batch —
  no QA slips** (additive cross-links all in-batch; touzen variants folded by attachment-pattern rule).
  · **batch 63** (N2 common — を-scope/focus/exception particles + と-simultaneity/listing + どころ-contrast,
  10 indexed): **を-scope:** をめぐって／めぐる (contested issue 'over/concerning', ↔ について neutral-topic;
  adnominal をめぐる; **med→high**) · を中心として／に (focal point 'centering on', ↔ をめぐって contention-
  vs-hub; **med→high**) · を除いて (formal 'except for', ↔ 以外 everyday; を除けば note) · 抜きで ('without'
  a normally-included thing, ↔ なしに plain; 冗談抜きで idiom) · 自体 ('itself/in itself' for things, ↔ 自身
  for people; **med→high**). **と-simultaneity/listing:** とともに (**2-sense** accompaniment / gradual
  parallel-change, ↔ と同時に instant) ↔ と同時に (**2-sense** same-instant / two-facets, ↔ とともに gradual /
  ながら one-subject) · といった ('such as', leads INTO a category head-noun, ↔ など closes-list / や loose-
  list). **どころ-contrast pair:** どころか ('far from A, opposite B', reverses expectation, ↔ かえって adverb)
  ↔ どころではない ('no time/room for ~', circumstances rule out, ↔ どころか / ている場合じゃない casual). Anchored
  to enriched ni-tsuite/o-chushin-ni/igai/nashi-ni/jishin/nagara/nado/ya/to-iu/kaette/teiru-baai-janai.
  **Deferred (next batch):** というような/というように (to-iu-youna/youni — overlap といった, defer). Clean batch,
  no QA slips. **Bumps:** megutte-meguru/o-chushin-to-ni-shite/jitai med→high.
  · **batch 64** (N2/N3 common — discourse connectives + は-topic restriction + risk/tendency modality +
  degree-limiting, 18 indexed): **discourse connectives** それに ('besides', same-direction add, ↔ そして
  sequence / その上 formal / それなのに flips) · それなのに ('and yet', reproachful contradiction, ↔ のに
  clause-internal / それにしても / しかし neutral) · それにしても ('even so', half-concede then marvel at
  excess, ↔ それなのに / とにかく) · 逆に ('conversely', genuine reverse ↔ かえって backfire / むしろ better-fit)
  ↔ かえって ('on the contrary', ironic reversal of intended effect ↔ 逆に broad / むしろ) · 要するに
  ('in short', boil-down summary, ↔ つまり rephrase; can sound blunt) · 従って ('therefore', formal logical
  conclusion, ↔ だから register / 要するに restate-vs-derive; **homograph に従って disambiguated**) · ちなみに
  ('incidentally', related aside ↔ それに same-argument-add) · あるいは ('or/alternatively', formal ↔ または
  plain-choice / それとも question). **は-topic restriction "setting aside / not to mention":** はともかく
  ('setting aside', colloquial-dismissive ↔ は別として formal) ↔ は別として ('apart from', neutral-defer,
  takes 〜かどうか; ↔ 以外 set-membership-vs-topic) · はもちろん ('A of course, and B too', ↔ だけでなく neutral /
  はもとより formal-twin) ↔ はもとより ('not to mention', formal/literary twin of はもちろん). **risk/
  tendency modality (extends 可能性がある web):** 傾向がある ('tends to', neutral statistical ↔ がち negative-prone /
  やすい easy-to) · 危険性がある ('risk that', clinical/technical ↔ 恐れがある forecast / 可能性 neutral) ↔ 恐れがある
  ('danger that', forecast/warning, negative-only ↔ 可能性 neutral / 危険性 clinical). **degree-limiting:**
  に過ぎない ('no more than', dismissive deflation ↔ だけ neutral-limit / 単に adverb-pairs) ↔ 単に ('simply',
  adverb wanting closing だけ/に過ぎない; **単なる before nouns** ↔ ただ everyday). Anchored to enriched soshite/
  sono-ue/noni/shikashi/tonikaku/mushiro/tsumari/dakara/mata-wa/soretomo/igai/dake-de-wa-naku/gachi/yasui/
  kanousei-ga-aru/dake/tada. **Slug notes:** または = `mata-wa`, しかも = `shika-mo`. Self-contrast caught
  (wa-tomokaku → moved to notes). Clean build, no QA slips.
  · **batch 65** (N2 common — ては warning/prohibition + "only after/by" emphatic + "without" set + formal
  に scope/span + standpoint/accordance に + increasing-degree adverbs, 17 indexed): **ては
  warning/prohibition:** ては ('if/whenever ~ → bad result', result-clause-negative-only; ちゃ/じゃ contractions,
  ↔ と neutral / てはいけない fixed-ban) ↔ ていては (ている under ては, 'if you keep ~ing', stresses duration,
  ↔ ては single-act / ている) · てはならない (formal/grave 'must not', rules/principles, ↔ てはいけない everyday /
  ては open-warning). **"only after/by" emphatic:** てはじめて ('only after / not until', main clause =
  realisation, ↔ てから neutral-order / てこそ) ↔ てこそ ('only BY ~ing', sole necessary MEANS→good result,
  +あってこそ, ↔ からこそ reason / こそ bare-emphatic). **"without" set:** なしに ('without', noun-based formal,
  Vることなしに, ↔ ないで spoken / ことなく) ↔ ことなく ('without ~ing even once', dict-form, written-emphatic,
  ↔ ないで / なしに) ↔ ずに済む ('get by without', relief-at-avoiding-burden, せずに済む irregular, ↔ ずに plain /
  ないで; 〜ずに済まない separate). **formal に scope/span:** において ('in/at', formal place/time/domain,
  における adnominal, ↔ で everyday, can't mark means) · にわたって ('over/throughout', full-coverage of span,
  にわたる adnominal, ↔ にかけて vague-edge / まで endpoint) · につき (**2-sense** 'per' rate / formal 'due to'
  notices; **disambig from について topic**). **standpoint/accordance に:** にしたら ('from ~'s standpoint',
  person's emotional viewpoint, にすれば/にしてみれば variants, ↔ にとって importance-eval / からすると infer-from-
  basis) · に従って (**2-sense** obey rule / 'as ~ proceeds' proportional, に従い formal; homograph 従って
  'therefore'; ↔ につれて gradual-only / に応じて match-conditions). **increasing-degree adverbs:** ますます
  ('more and more', existing trend snowballing, ↔ 一層 / さらに) ↔ 一層 ('even more', one deliberate step up,
  formal, より一層, ↔ ますます / もっと) · よほど ('considerably', inferred-degree + conjecture, よっぽど casual,
  ↔ かなり flat-fact / あまり 'not very' trap) · 実に ('truly/indeed', heartfelt evaluative emphasis on adj;
  disambig 実は 'actually'; ↔ 本当に everyday / とても neutral). Anchored to enriched to-conditional/
  te-wa-ikenai/te-iru/te-kara/kara-koso/koso/nai-de/zu-ni/de/ni-kakete/made/ni-tsuite/ni-totte/kara-suru-to/
  ni-tsurete/ni-oujite/sara-ni/motto/kanari/amari/hontou-ni/totemo. **Slug notes:** に応じて = `ni-oujite`
  (not ni-ojite). Clean build, no QA slips.
  · **batch 66** (N2 common — manner/likeness という set + superlative/at-any-rate emphasis + concessive
  even-if/despite + evaluative/degree adverbs + almost/somehow/carelessly, 18 indexed + 1 redirect):
  **manner/likeness:** 風に ('in the manner of', colloquial style, こんな風に / 〜風 noun-suffix 'style',
  ↔ ように broad) ↔ という風に (cite clause/quote as manner, ↔ 風に bare / というように) · というように (cite
  manner/example-pattern / 'as if to say', adverbial, ↔ といった category-head / というような) ↔ というような
  ('such ~ as', **adnominal→NOUN**, ↔ といった crisp / というように adverbial) · かのように ('as if', explicitly
  counter-to-fact, まるで〜かのように, ↔ かのようだ predicate / ように maybe-real). **superlative/at-any-rate:**
  何より ('more than anything', 〜で何よりです relief, 何よりの+N, ↔ 一番 ranked-set / 何といっても) ↔ 何といっても
  ('above all', say-what-you-will standout, ↔ 何より / とにかく) · 何しろ ('after all, you see', overriding
  reason +から/ので, なにせ/なんせ variants, ↔ とにかく opposite-job) ← **なにしろ kana → noindex redirect → nani-shiro**.
  **concessive:** であっても (formal 'even if it is', N/な-adj, どんな〜, ↔ でも casual / ても verb) · くせして
  ('even though' WITH reproach, casual rougher くせに, same-subject, ↔ くせに / のに neutral) · もかまわず
  ('heedless of', actor ignores what they should mind, 構う-neg, 〜のもかまわず, ↔ にもかかわらず fact-despite).
  **evaluative/degree adverbs:** 案外 ('unexpectedly', mild relief, ↔ 意外と sharper; 以外 trap; **med→high**) ·
  幸い ('fortunately'; 〜ば幸いです polite-request sense) · 少なくとも ('at least', lower floor, ↔ せめて wish /
  せいぜい upper-cap) · わずかに ('slightly', narrow margin, ↔ わずか noun/な-adj). **almost/somehow/carelessly:**
  もう少しで ('almost', near-miss +ところだった, ↔ ところだった predicate / そうになる on-verge) · どうにか ('somehow
  manage', どうにかなる, ↔ なんとか everyday / どうか 'please' trap) · うっかり ('carelessly', lapse-of-attention
  +てしまう, ↔ つい weakness-of-will; **med→high**). Anchored to enriched youni/to-itta/ka-no-you-da/ichiban/
  tonikaku/de-mo/te-mo/kuse-ni/noni/ni-mo-kakawarazu/igai-to/semete/seizei/wazuka/tokoro-datta/sou-ni-naru/
  nan-to-ka/dou-ka/tsui. **Confidence bumps:** angai/ukkari med→high. **Adnominal vs adverbial split:**
  というような(→N) vs というように(→V) taught explicitly, both ↔ といった. Clean build, no QA slips.
  · **batch 67** (N2 common — inference/seeming/opinion modality + wish + hearsay, 5 indexed + 1 redirect;
  focused tail batch near context ceiling): 思{おも}われる (spontaneous れる 'it seems / is thought',
  impersonal-formal, ↔ と考えられる reasoned / れる・られる spontaneous family; plain-passive 'be regarded'
  note; **med→high**) ↔ と考{かんが}えられる (reasoned impersonal conclusion, ↔ と考えられている established-view /
  思われる impression) · のではないだろうか (softened assertion-as-question 'isn't it perhaps?', のではないでしょうか
  polite, ↔ のだろうか genuine-wonder / じゃないか blunt) · たらいいのに ('I wish ~ but it isn't so', regret-のに,
  ↔ ばいい suggestion / ばよかった past-regret / といい uncontrolled-hope) · とか(で) (sentence-end hearsay/
  vague-report, distinct from listing とか; とかで 'and for that reason', ↔ そうだ straightforward-hearsay /
  って direct-relay / とか listing; **med→high**). **te-shou-ga-nai (てしょうがない) → noindex redirect →
  te-shikata-ga-nai** (casual しかた→しょう contraction; resolves the long-pending batch-46/58 fold candidate).
  Anchored to enriched rareru/to-kangaerarete-iru/darou-ka/no-darou-ka/janai-ka/ba-ii/ba-yokatta/to-ii/
  souda/tte/toka/te-shikata-ga-nai. **Confidence bumps:** omowareru/toka-2 med→high. **Reasoned-vs-impression
  split:** と考えられる (analytic) vs 思われる (natural impression) taught. Clean build, no QA slips.
  · **batch 68** (N1 common — appropriate-to-nature 'in one's own way' + irreversible-state adverb, 2 indexed
  + 2 redirects; small tail batch at context ceiling): なりに ('in one's own way / suited to one's level',
  modest-effort-within-limits; **adverbial なりに / adnominal なりの both taught**; それなりに set-form note;
  ↔ らしい befitting-from-outside) ← **なりに／なりの (nari-ni-no) → noindex redirect → nari-ni** (same pattern,
  に/の slot variants) · もはや (formal/literary 'by now / no longer', irreversible point-of-no-return,
  ↔ もう everyday). **のことだから (no-koto-da-kara) → noindex redirect → koto-dakara** (のことだから IS the
  canonical full form of ことだから 'predict from known character', batch-21 enriched — dedup fold). Anchored
  to enriched rashii/mou/koto-dakara. Clean build, no QA slips. **Session batches 64–68: 764 → 824
  (+60 indexed).**
  · **batch 69** (N3 common — distributive 'each', 1 indexed; single-node batch at context ceiling):
  それぞれ ('each / respectively', individual distinctness within a group; それぞれの+N; ↔ ずつ equal-share /
  ごとに per-unit; めいめい/各自 synonym note). Anchored to enriched zutsu/goto-ni. Clean build, no QA slips.
  **Session batches 64–69: 764 → 825 (+61 indexed).**
  · **batch 70** (mixed common grab-bag — approximation/portion particles + aspect/sequence + contrast +
  adverbials + basis/dependency connectives + 'some-kind-of', 17 indexed + 3 redirects): **approximation/
  portion/range** — あたり (approximate point in space/time/quantity 'around', ↔ ごろ time-only / ぐらい
  amount; 'someone like ~' note) · 分〔ぶん〕 (corresponding portion/share, ↔ ぐらい rough-vs-exact; その分
  'correspondingly' note) · のうち(で) (select from a bounded set 'among/of', ↔ の中で everyday / うちに
  time-window) · **kurai → noindex redirect → gurai** (くらい/ぐらい fold pair, gurai owns teaching).
  **aspect/sequence** — かと思うと (no-sooner-than/surprising next event, V-た base, speaker-observed
  restriction ↔ た途端 single-instant / や否や literary) · つつある (change in progress toward endpoint,
  formal, change-verb restriction ↔ ている neutral-ongoing) · た末(に) (long effortful process → final
  outcome, ↔ た途端 instant / 後で neutral-after; あげく negative-result note). **contrast** — 一方(で)
  ('on one hand/meanwhile', two coexisting facts ↔ 反面 same-thing-two-sides / に対して head-to-head /
  **一方だ one-way-trend disambiguated**) · **to-iu-yori-wa → noindex redirect → to-iu-yori** (は-variant) ·
  いわゆる ('so-called', 連体詞 pre-noun, no conjugation). **adverbials** — 万が一 (remote serious
  possibility 'in the unlikely event', fronts conditional ↔ もし(も) neutral; 万が一の adnominal note) ·
  あらかじめ ('beforehand', formal, pairs ておく; 前もって/事前に synonyms) · 何から何まで ('everything,
  A-to-Z', emphatic から〜まで frame, gratitude/complaint). **basis/dependency** — にかかっている ('depends
  on/hinges on', clause-は + 決め-factor-に ↔ によって varies-by) · を踏まえて ('based on/taking into
  account', weigh-prior-facts, formal ↔ に基づいて strict-standard / をもとに raw-material) · がきっかけで
  ('triggered by', single triggering incident ↔ によって neutral-cause; をきっかけに note) · に関わる
  ('be a matter of/gravely affect', high-stakes ↔ について mere-topic; everyday 'get involved' note) ·
  いずれにしても ('in any case/either way', same result whichever option ↔ とにかく brush-aside; どちらに
  しても synonym). **some-kind-of** — 何らかの ('some (kind of)', adnominal→noun, asserts existence,
  formal; 何か pronoun + なにかの reading variant notes) ← **nani-ka-no → noindex redirect → nanraka-no**.
  Anchored to enriched goro/gurai/no-naka-de/uchi-ni/ta-totan/ya-ina-ya/te-iru/ato-de/hanmen/ni-taishite/
  ippou-da/to-iu-yori/moshi-mo/ni-yotte/ni-motozuite/o-moto-ni/ni-tsuite/tonikaku. **QA catches (pre/at
  build):** dropped a self-referential empty contrast in ni-kakatteiru; moved 何か comparison to notes
  (nani-ka slug doesn't exist); fixed duplicate `confidence:` key in nanraka-no (seed had med, added high
  — build error 'duplicated mapping key', resolved to single high). **Threshold drop:** context_gate.py
  continue-threshold lowered 250k → 190k (user directive). **Session batch 70: 825 → 842 (+17 indexed).**
  · **batch 71** (mixed common grab-bag — additive 'also/even' particles + concession/premise connectives +
  respect/famous/state + worth/leverage/experience idioms + care/entrust idioms + interval/every-time +
  means/both-and connectives + emphatic topic, 17 indexed + 1 redirect): **additive** — も又〔もまた〕 ('~ too',
  formal/literary ↔ も plain) · にも (particle stack に+も 'also/even to'; question-word+neg sweep restriction
  ↔ も replaces-が/を; **low→high**, transparent stack). **concession/premise** — とは言うものの ('having said
  that', calm reasoned ↔ とはいえ compact / ものの clause-internal / のに emotional) · を前提に ('on the premise
  of', assumed condition going-in ↔ を踏まえて facts-weighed). **respect/famous/state** — 点で ('in the respect
  that', single criterion ↔ において broad-field; 点 noun + という点で clause-attach) · は〜で有名 ('A famous for
  B', B takes で-not-を restriction; ことで for clauses; として 'famous as') · は〜となっている ('has become / is
  set as', formal established-state ↔ となる the-event / ている everyday になっている). **worth/leverage/experience**
  — 甲斐〔がい〕 ('worth ~ing', V-stem+がい rendaku / Nの甲斐 unvoiced; 生きがい・やりがい fixed) · を活かす ('make
  the most of', maximize-inherent-asset ↔ を使って plain-use; 生かす kanji note) · 思いをする ('have a ~
  experience', emotion-adj+思いをする, usually unpleasant, undergone; させる causative; vs 経験する neutral).
  **care/entrust** — に気をつける ('be careful about', thing-に restriction ↔ に気がつく notice-vs-caution つく/
  つける) · を〜に任せる ('leave A to B', AをBに role-order restriction; 運を天に任せる idiom). **interval/every-time**
  — ぶり (**2-sense** ①interval-noun 三年ぶりだ ②manner-suffix 仕事ぶり/話しぶり; ↔ ぶりに adverbial-interval; **med→
  high**) · 度に ('every time', each-occasion-triggers ↔ ごとに regular-unit / おきに gap-between). **means/both-and**
  — ことにより/によって ('by ~ing', formal-written nominalized-means ↔ ことで spoken / によって noun-means) · も〜ば
  〜も ('both A and B', ば-frame cumulative-grounds ↔ も〜も plain-pair / し reason-stack). **emphatic topic** —
  ったら (sentence-head topic with exasperation/affection, casual ↔ って neutral-topic / は plain-topic; distinct
  from conditional たら). **te-wa-ikenai-kara → noindex redirect → te-wa-ikenai** (compositional てはいけない+から).
  Anchored to enriched mo/mo-2/mata/to-wa-ie/mono-no/noni/o-fumaete/ni-oite/to-naru/te-iru/o-tsukatte/
  ni-ki-ga-tsuku/buri-ni/goto-ni/oki-ni/koto-de/ni-yotte/mo-mo/shi/tte/wa/te-wa-ikenai. **QA catches (×4):**
  stray 評価 kanji inside an English distinction string (ten-de) — removed; a typo `attaping_to:` duplicate key
  in ni-ki-o-tsukeru formation — removed; duplicate `confidence:` key in buri (seed med + added high → build
  'duplicated mapping key') — resolved to single high. **NEW GOTCHA → §4:** the seed frontmatter ALREADY
  carries `confidence:` — when bumping it, EDIT the existing line, never add a second (silent until build
  fails 'duplicated mapping key'). Bit this twice (nanraka-no b70, buri b71). **Session batch 71: 842 → 859
  (+17 indexed).**
  · **batch 72** (deferred catalog-fold resolutions — drains the meaningful common band, 1 indexed + 3
  redirects): resolved the long-pending fold decisions PASS flagged. **o-suru → noindex redirect → o-suru-2**
  (o-suru-2 N4 was already the enriched canonical お〜する humble; o-suru N3 is the duplicate). **yaru → noindex
  redirect → te-yaru** (てやる benefactive 2-sense already owned by enriched te-yaru). **yaru-3 ENRICHED** as
  the genuine standalone main verb やる = casual する 'to do/play' (宿題をやる/サッカーをやる/店がやってる
  'is open'; ↔ てやる auxiliary-benefactive; **no standalone する node** — する is neutral, やる its casual
  counterpart; 花に水をやる 'give to plant' note; **low→high**). **naze-nara-ba-kara-da → noindex redirect →
  nazenara** (なぜなら(ば)〜からだ frame; ば optional formal flourish, からだ closer — all owned by enriched
  nazenara). Anchored to enriched o-suru-2/te-yaru/nazenara. **Common band now effectively DRAINED:** all
  remaining `--freq common` stubs are resolved noindex redirect-hubs (batch-12/15/19/21/35/36/37/40/42/58/60/
  61/62/66/68 folds) that reappear in the worklist by design — no pending enrichment work left in `common`.
  **Next band = `uncommon`** (`python3 scripts/list_stubs.py --freq uncommon`). Clean build, no QA slips.
  **Session batch 72: 859 → 860 (+1 indexed).**
  · **batch 73** (uncommon band opener — casual sentence-final question particles, 2 indexed): かい (warm/
  familiar yes/no question, softer than か; **yes/no only** restriction — question-word questions take だい;
  older/male tone ↔ だい question-word-partner / か neutral) · かね (musing 'I wonder', か+ね thinking-aloud or
  inviting agreement; older/masculine ↔ かな everyday-all-ages / か direct). Anchored to enriched dai/ka/kana.
  Tight self-contained pair (sentence-final particle family). Clean build, no QA slips. **Session batch 73:
  860 → 862 (+2 indexed). Session total (b70–73): 825 → 862 (+37 indexed).**
  · **batch 74** (uncommon band — partial/quantity negation + だけ befitting/merit web + こと exclamatory +
  'so to speak'/'for some reason' adverbs, 18 indexed): **partial/quantity negation** — the **は-partial trio**
  全部は〜ない ('not all', は narrows 'not' to part — without は = 'none at all') ↔ みんな〜ない ('not everyone',
  same は-logic for people — bare みんな来ない can read 'no one') ↔ いつもは〜ない ('not always/usually', frequency
  axis); めったに〜ない ('seldom', negative-locked ↔ あまり〜ない milder / 全然 absolute) · 〜ない〜はない (double-neg
  universal 'there's no ~ that doesn't ~' = every ~ does; ≠ 〜ないことはない hedged-partial note). **だけ
  befitting/merit web** (all off enriched dake; pivots on さすが/dake-de-wa-naku) — だけあって ('as you'd expect,
  fittingly', positive result ↔ だけに) ↔ だけに ('precisely because, all the more', intensifies + allows
  NEGATIVE outcomes, ↔ からこそ pure-reason) ↔ だけのことはある (sentence-final verdict 'no wonder ~', often
  さすが〜; ↔ さすが adverb) ↔ だけのことはあって (て-form connective of the verdict); だけましだ ('at least ~ is
  better', bad-situation saving-grace ↔ ましだ bare-preferable) ↔ だけ(のこと)だ ('it's simply a matter of ~,
  that's all', downplay ↔ だけだ plain-only). **こと exclamatory** — ことか ('how very ~!', rhetorical
  question-word exclamation, emotional/literary, ↔ どんなに〜ことか / どれほど〜ことか) ↔ どんなに〜(こと)か (どんなに
  instance; **vs どんなに〜ても concessive — same どんなに, exclamation-vs-condition trap**) ↔ どれほど〜(こと)か
  (どれほど instance, extent-leaning). **'so to speak' pair** 言わば (written/compact, pairs 〜のようなものだ) ↔
  言ってみれば (spoken/tentative; ↔ つまり precise-restate vs figurative-paraphrase). **'for some reason' pair**
  どういうわけ(だ)か (puzzling-circumstance, formal) ↔ どうして(だ)か (casual; **vs plain どうして 'why?' — trailing
  か makes it a statement not a question**) — both ↔ なぜか compact-everyday. Anchored to enriched metta-ni/
  amari/zenzen/dake/dake-da/dake-de-wa-naku/kara-koso/sasuga/mashida/koto/donnani/donna-ni-temo/tsumari/
  naze-ka/nai-form. **Confidence bumps:** metta-ni-nai low→high, zenbu-wa-nai/itsumo-wa-nai/dake-no-koto-wa-atte/
  donnani-koto-ka/dorehodo-koto-ka/dou-iu-wake-da-ka/doushite-da-ka/nai-wa-nai med→high; minna-wa-nai low→med
  (review_reason: partial-reading hinges on は). **Slug notes:** ましだ = `mashida` (not mashi-da); bare
  `dorehodo` has no node (cross-link within batch). Clean build, no QA/lint slips. **Opens the uncommon band's
  first real cluster-group (batch 73 was the 2-node opener). Session b73–74: 860 → 880 (+20 indexed).**
  · **batch 75** (uncommon band — temporal-span 'as long as/until end' + 'as for/instead of' connectives +
  か either-or/whether + degree/quantity は + N4 conditional/potential + futility, 14 indexed): **temporal
  span** — 〜間は ('throughout the span', continuous state; **間は throughout vs 間に point-within** taught) ↔
  うちは ('as long as the state lasts', +'before it changes' nuance ↔ うちに action-timing) · 最後まで ('to the
  very end', emphatic まで + perseverance verbs ↔ まで plain-endpoint; low→med) · までで ('up through ~, that's
  the cutoff', で frames endpoint as stopping-line ↔ まで range / までに deadline). **connectives** — に関しては
  ('as for ~ in particular', は-topic-emphasis variant of に関して ↔ について everyday) · に代わって ('instead of/
  on behalf of', formal replacement ↔ 代わりに broad / の代わりに everyday). **か either-or/whether** —
  か〜かどちらか ('either ~ or ~', exactly-two-pick ↔ か〜か listing / か〜ないか yes-no) · かは〜によって違う ('whether
  ~ varies by ~', embedded-Q + によって違う frame ↔ によって; med, compositional). **degree/quantity は** —
  あまり(に)〜/あまりの〜に ('so ~ that', excess→consequence; **あまり〜ない reductive vs あまりに〜 intensifying** —
  same word opposite direction ↔ すぎる; med→high) · 〔数量〕は ('at least ~', は on affirmative quantity = floor;
  **vs 全部は〜ない partial-negation — affirmative-floor vs negative-partial** ↔ ぐらい estimate) · 〜は〜くらいです
  ('~ is about ~', polite ballpark frame ↔ くらい/ぐらい). **N4** — だら／だったら (casual copula conditional 'if
  it is ~'; だら colloquial/regional contraction as variant; ↔ なら premise / たら verb-conditional; low→med,
  review_reason) · 聞ける (potential of 聞く 'can hear/can ask'; **聞ける ability/opportunity vs 聞こえる involuntary-
  audible** ↔ れる/られる; low→high). **futility** — 〜ても仕方がない ('no use ~ing', action-futility; **THE trap:
  ても仕方がない 'no use doing' vs てしかたがない 'can't help feeling'** ↔ 仕方がない situation-resignation / ても base).
  Anchored to enriched aida-ni/uchi-ni/made/made-ni/ni-kanshite/ni-tsuite/kawari-ni/no-kawari-ni/ka-ka/ka-nai-ka/
  ni-yotte/amari/sugiru/gurai/nara/tara/kikoeru/reru/shikata-ga-nai/te-shikata-ga-nai/te-mo. **Confidence bumps:**
  metta… no — aida-wa/made-de/ni-kanshite-wa/ka-ka-dochiraka med→high, amari-2 med→high, suuryou-wa/wa-kurai-desu
  med→high, kikeru low→high, saigo-made/dara low→med, minna… (n/a). **Slug notes:** ぐらい owner = `gurai`
  (kurai redirects); どちらか/ru-tokoro have no node (cross-linked within batch / prose). Clean build, lint clean
  (14), scan clean. **Session b73–75: 860 → 894 (+34 indexed).**
  · **batch 76** (uncommon band — ばかり aspect/connective web + 'even' emphatic, 4 indexed; tight batch
  near context ceiling): **ばかり web** (all off enriched bakari) — ばかりだ (**2-sense** ①one-way trend
  'only keeps ~ing', change-verbs, ↔ 一方だ near-syn / ている neutral ②'all that's left is to ~', あとは〜) ·
  ばかりか〜(さえ) ('not only ~ but even ~', literary escalation with surprising 2nd item ↔ だけでなく everyday /
  ばかりでなく / さえ) · ばかりに ('simply because ~', single cause → regrettable BAD result restriction ↔ から
  neutral / ので; せいで note). **'even' emphatic** — ですら ('even ~', literary/emphatic ↔ でさえ everyday /
  すら bare / さえ neutral). Anchored to enriched bakari/ippou-da/te-iru/dake-de-wa-naku/bakari-de-wa-naku-3/
  sae/kara/node/de-sae/sura. Clean build, lint clean (4), scan clean. **Session b73–76: 860 → 898 (+38 indexed).**
  · **batch 77** (uncommon band — self-contained N2 suffix/adverb, 2 indexed; minimal batch at context ceiling):
  〜同士 ('among/between fellow ~ / each other', reciprocal-suffix on same-type nouns; 似た者同士 set phrase /
  お互いに note) · どこまでも ('endlessly / to the very end / thoroughly', literal 'no matter how far' →
  'utterly'). Both genuinely self-contained — no confusable sibling node exists (tagai-ni/doko-mo/aku-made-mo
  all absent), so `contrasts` correctly empty (§6-B). **Bumps:** doushi/doko-made-mo med→high. Clean build,
  lint clean (2), scan clean. **Milestone: 900 indexed. Session b73–77: 860 → 900 (+40 indexed).**
  · **batch 78** (uncommon band — こそあ-した demonstratives + definition/restatement frames + "no choice
  but to"/"nothing but" web + いられない modality, 13 indexed + 2 conservative-noindex + 2 redirects):
  **こそあ-した set** — ああした (あ-series 'that kind, removed/mutually-known', formal vs ああいう) ↔ そうした
  ('that kind, in shared context', most common in writing vs そういう) — both laddered against enriched
  kou-shita/kou-itta/sou-iu. **definition/restatement** — 前者は・後者は (the former/the latter, exactly-two-
  in-order, written-only ↔ repeat-nouns in speech) · というのは事実だ (assert truth 'it is a fact that', という
  droppable ↔ to-iu-no-wa def/reason / no-da background) · というのは〜ことだ (define a named term 'X means' ↔
  tsumari restate / no-wa-no-koto-da no-という variant) · **のは〜のことだ (LOW conf → conservative, stays
  noindex)** (cleft 'what ~ refers to is' ↔ no-wa-da / to-iu-no-wa-koto-da) · **ことなのだ (LOW conf →
  conservative, stays noindex)** (こと+な+のだ 'the point is ~', compositional overlap with no-da). **"no
  choice but to" / "nothing but" web** (all off enriched shika-nai/igai/hoka) — よりほかない (canonical 'no
  choice but to', formal vs しかない everyday; **med→high**; covers の/は variants) ← **よりほかない-2 → noindex
  redirect → yori-hoka-nai** (bare-spelling true-dup) · よりしかたがない (identical meaning, しかた vs ほか lexical
  swap ↔ yori-hoka-nai) · 以外にない (noun 'nothing but X' + verb 'no choice but to do', **med→high**) ·
  のほか(に)(は)〜ない (canonical 'none but ~', いる→いない people / ある→ない things, **med→high**) ← **のほかに〜ない
  → noindex redirect → no-hoka-ni-wa-nai** (は-less dup). **いられない modality** — the **trap trio**: ずにはいられ
  ない ('can't help DOING', involuntary urge, する→せずに restriction; ↔ ないではいられない same-meaning ないで-form
  twin) ↔ ないではいられない ('can't help but', ないで-base, softer/spoken vs ずに formal) ↔ **てはいられない ('can't
  AFFORD to keep ~ing', no-time-to-remain — opposite stance from ずにはいられない despite similar shape)** ↔
  てばかりはいられない ('can't keep just ~ing', ばかり adds over-indulgence ↔ te-wa-irarenai). Anchored to enriched
  kou-shita/kou-itta/sou-iu/no-wa-da/to-iu-no-wa/tsumari/no-da/koto-da/shika-nai/igai/hoka/yori/nai-form/
  zu-ni/bakari/te-shikata-ga-nai/te-tamaranai. **Folds:** yori-hoka-nai-2→yori-hoka-nai, no-hoka-ni-nai→
  no-hoka-ni-wa-nai (both stay noindex). **Confidence bumps:** yori-hoka-nai/igai-ni-nai/no-hoka-ni-wa-nai/
  te-bakari-wa-irarenai med→high. **Missing-target avoided:** sono-you-na & te-ageru don't exist (Explore
  brief flagged) — routed cross-links to sou-iu / sashiageru instead. Clean build, lint clean (17), scan clean.
  **Session batch 78: 900 → 913 (+13 indexed).**
  · **batch 79** (uncommon band — ない double-negative hedge modality + whether-or にしろ/にしても/なり set +
  "even if one wanted to, can't" potential-concession, 11 indexed + 3 redirects): **ない double-negative
  hedge** (cautious half-yes / faint possibility) — ないこともない (canonical 'it's not impossible / I suppose ~',
  nuance fires: deliberate understatement; ← **ないことも／はない nai-koto-mo-wa-nai → noindex redirect**, は-firmer/
  も-softer variant) ↔ なくもない (compact casual, なく continuative, ↔ feeling verbs 分からなくもない) ↔ ないでもない
  (ないで-form, clings to feeling/thinking verbs) ↔ ないものでもない (formal/literary, +condition しだいでは) · ない
  とも限らない (DIFFERENT: 'can't rule out it WON'T happen', warns of risk → precaution; ↔ とは限らない denies-
  general-assumption double-neg twist). **whether-or set** — にしろ (canonical 'whether/even if', from imperative
  しろ, formal ↔ にしても softer / としても hypothetical; now enriched, was the batch-53 anchor stub) ↔ にしろ〜
  にしろ ('whether A or B → same conclusion' ↔ にしても〜にしても softer / なり〜なり choose-one / か〜か neutral-list)
  ↔ にしても〜にしても (everyday softer twin) ↔ なり〜なり (offers options to CHOOSE one and act, advice nuance;
  **distinct from literary なり 'the moment ~'** [[nari]]). **potential-concession** — ようにも〜ない ('even if
  one wanted to, can't', volitional+にも+potential-neg of SAME verb, external blocker restriction; **med→high**;
  ← **（よう）にも〜ない nimo-nai → noindex redirect** exact dup) ↔ どうにも (adverb '(with neg) just can't / no
  way', どうにもならない idiom; ← **どうにも〜ない dou-ni-mo-nai → noindex redirect** どうにも always takes neg).
  Anchored to enriched koto/nai/nai-de/nai-form/volitional-form/to-wa-kagiranai/ni-shite-mo/to-shite-mo/te-mo/
  ka-ka/dou-ka. **Folds (stay noindex):** nai-koto-mo-wa-nai→nai-koto-mo-nai, nimo-nai→you-ni-mo-nai,
  dou-ni-mo-nai→dou-nimo. **Confidence bump:** you-ni-mo-nai med→high. **Anchor note:** なり (as-soon-as) ≠
  listing なり〜なり — did NOT cross-link them. Clean build, lint clean (14), scan clean. **Session batch 79:
  913 → 924 (+11 indexed). Session b78–79: 900 → 924 (+24 indexed).**
  · **batch 80** (uncommon band — まで "simply/merely" + "that's the end of it" modality, 5 indexed; tight
  batch near context ceiling): **"simply/merely a matter of"** — までだ／までのことだ (canonical 'it's simply a
  matter of / nothing more to it', のこと emphatic, covers V-る resolve + V-た merely-did; nuance: dismissive/
  unfazed; ↔ dake-no-koto-da near-syn) ← splits into the **tense-pinned pair** るまでだ ('if it comes to it,
  I'll simply ~', forward resolve, composure nuance ↔ たまでだ) ↔ たまでだ ('I merely ~ed, nothing more',
  backward motive-deflection, defensive/modest nuance ↔ dake-da). **"that's the end of it"** — それまでだ
  (resigned finality 'point of no return', warning nuance ↔ made-no-koto-da fallback-vs-deadend) ↔ ばそれ
  までだ (explicit ば-condition frame 'if ~, it's all over', pointed warning ↔ それまでだ bare / ば-conditional
  total-loss-result). Both まで sub-senses cross-linked (まで as 'only that far' vs 'up to there, no further').
  Anchored to enriched made/dake-no-koto-da/dake-da/ba-conditional. Clean build, lint clean (5), scan clean.
  **Session batch 80: 924 → 929 (+5 indexed). Session b78–80: 900 → 929 (+29 indexed).**
  · **batch 81** (uncommon band — N1 standpoint pair + "forced to / compel" passive-causative pair, 4
  indexed): **standpoint pair** — にしてみれば ('from ~'s point of view / if you put yourself in ~'s shoes';
  the てみる adds 'imagine being in their shoes' over plainer にしたら ↔ ni-shitara near-syn / ni-iwasereba
  voiced-opinion / ni-totte importance-eval) ↔ に言わせれば ('if you ask ~ / in ~'s opinion', voices the
  OPINION the person would state, 私に言わせれば = assert own view forcefully; causative 言わせる+ば, variant
  に言わせると; ↔ ni-shite-mireba felt-vs-spoken / ni-yoru-to neutral-source-vs-opinionated). **forced/compel
  pair** (formal/written, 余儀{よぎ}なく + する-noun outcome) — を余儀なくされる ('be forced to / compelled
  into', PASSIVE, victim is subject, impersonal-circumstance cause ↔ o-yoginaku-saseru mirror / zaru-o-enai
  verb-based-everyday / nakereba-naranai obligation-vs-loss-of-choice) ↔ を余儀なくさせる ('compel/force into',
  CAUSATIVE, impersonal cause is subject + person-に, rarer than the passive ↔ o-yoginaku-sareru mirror /
  saseru person-will-vs-circumstance). Anchored to enriched ni-shitara/ni-totte/ni-yoru-to/saseru/
  zaru-o-enai/nakereba-naranai. **Mirror-pair teaching:** される victim-subject ↔ させる cause-subject made
  explicit on both; passive される flagged as the far-more-common form. Clean build, lint clean (4), scan
  clean. **Session batch 81: 929 → 933 (+4 indexed).**
  · **batch 82** (uncommon band — formal occasion / "prior to" / "after (much)" temporal connectives, 7
  indexed + 2 redirects): **occasion set** — に際して (formal/ceremonial 'on the occasion of', momentous
  one-time undertaking + speech-act ↔ sai-ni broader-formal / ni-atatte / toki everyday) ↔ に当たって
  ('on the occasion of / in undertaking', run-up + resolve to starting something; **disambig from に当たる
  'corresponds to'** ni-ataru ↔ ni-saishite near-syn) · 折 ('when', polite/warm, letters + seasonal
  greetings 寒さの折; ↔ sai-ni neutral-official / toki plain). **precedence set** — に先立って／に先立ち
  ('prior to', preparatory step bound to a main event, formal ↔ mae-ni neutral-before / ni-sakigakete) ↔
  に先駆けて ('ahead of OTHERS / be the first to', competitive pioneering nuance ↔ ni-sakidachi preparation-
  vs-competition / mae-ni). **after set** — あげく(に) ('after much ~, ending BADLY', prolonged troublesome
  process → regrettable result; **vs た末 neutral-outcome** ta-sue ↔ ato-de plain-after) · のち(に) (formal/
  literary 'after', notable later development ↔ ato-de everyday-register). **Folds (stay noindex):** 末に
  (sue-ni) → ta-sue (に-form of 〜た末/〜の末, true dup) · 際 bare-noun (sai) → sai-ni (the 際に construction).
  Anchored to enriched sai-ni/ni-ataru/toki/mae-ni/ta-sue/ato-de. **Anchor note:** 末 owned by ta-sue
  (slug, not sue-ni); あげく has no separate enriched node beyond ageku-ni (ta-sue's note pointed here).
  Clean build, lint clean (9), scan clean. **Session b81–82: 929 → 940 (+11 indexed).**
  · **batch 83** (uncommon band — goal/aim/turning-point を-connectives + "unless / without there can be
  no" conditional-negatives, 7 indexed + 3 redirects): **goal/aim:** を目指して ('aiming for', goal as a
  destination/end-point you head toward ↔ o-mokuhyou-ni benchmark) ↔ を目標に ('with the goal/target of',
  concrete measurable benchmark, takes こと-clause ↔ o-mezashite aspirational). **turning-point pair:**
  を機に ('taking ~ as an opportunity', shorter/everyday, deliberate new action ↔ o-keiki-ni formal /
  ga-kikkake-de neutral-trigger) ↔ を契機に ('taking ~ as a turning point', formal/literary, weighty/social-
  scale change ↔ o-ki-ni shorter / ga-kikkake-de). **unless/without conditional-negatives** (main clause
  must be negative/impossible): ないことには ('unless ~', names an indispensable precondition ↔ nakereba
  plain-if-not / te-hajimete positive-only-after-side) · なしでは ('without ~, … not', は-emphatic noun
  condition ↔ nashi-de neutral-lacking / nashi-ni-wa formal-twin) ↔ なしには ('without ~, … cannot', formal/
  written twin ↔ nashi-de-wa / nashi-ni plain-without-doing). **Folds (stay noindex):** をめぐって (o-megutte)
  → megutte-meguru (batch-63 dup) · を中心に (o-chushin-ni) → o-chushin-to-ni-shite (batch-63 に-variant) ·
  ないことには〜ない (nai-koto-niwa-nai) → nai-koto-ni-wa (negative main clause inherent). Anchored to enriched
  ga-kikkake-de/nakereba/te-hajimete/nashi-de/nashi-ni. **Anchor note:** をめぐって owned by megutte-meguru,
  を中心 by o-chushin-to-ni-shite (slugs, not the o-*-ni stubs). Clean build, lint clean (10), scan clean.
  **Session b81–83: 929 → 947 (+18 indexed).**
  · **batch 84** (uncommon band — conviction / "only natural" modality, 3 indexed; tight batch near
  context ceiling): にほかならない ('is nothing but / none other than / is precisely', emphatic exact
  identification ruling out other explanations, N + / 〜からにほかならない reason form; ↔ ni-suginai opposite-
  valence 'merely' / ni-chigainai guess-vs-assertion) · に相違ない ('there is no doubt that / must surely
  be', formal/literary near-certainty from grounds; ↔ ni-chigainai same-meaning-everyday-register /
  ni-hokanaranai guess-vs-equivalence) · のももっともだ ('it's only natural / no wonder', a reaction
  justified by circumstances, のも+もっともだ, empathetic; ↔ touzen-da expected-outcome / atarimae-da blunt-
  obvious). Anchored to enriched ni-suginai/ni-chigainai/touzen-da/atarimae-da. **Confidence bump:**
  no-mo-mottomo-da med→high (meaning standard, gate cleared). Clean build, lint clean (3), scan clean.
  **Milestone: 950 indexed. Session b81–84: 929 → 950 (+21 indexed).**
  · **batch 85** (uncommon band — rhetorical-denial modality pair, 2 indexed; lean batch at context
  ceiling): ものか ('there's no way ~! / as if!', emotional defiant rhetorical rejection — question shape =
  opposite meaning, takes no answer; もんか rougher; ↔ wake-ga-nai calm-logical-impossibility / hazu-ga-nai
  reasoned-can't-be) · ことにはならない ('it doesn't mean that ~', denies a logical CONCLUSION not a fact,
  often after からといって; ↔ wake-de-wa-nai general-denial-vs-amounts-to). Anchored to enriched wake-ga-nai/
  hazu-ga-nai/wake-de-wa-nai. Clean build, lint clean (2), scan clean. **Session b81–85: 929 → 952
  (+23 indexed).**
  · **batch 86** (uncommon band — それどころか escalating contrast, 1 indexed; single lean node at context
  ceiling): それどころか ('far from it / on the contrary / not only that', sentence-opener that denies the
  prior statement then escalates to a stronger opposite; ↔ dokoroka within-sentence-noun-attach vs
  standalone-opener / kaette ironic-reversal-of-effect vs escalate-past-denial). Anchored to enriched
  dokoroka/kaette. Clean build, lint clean (1), scan clean. **Session b81–86: 929 → 953 (+24 indexed).**
  · **batch 87** (uncommon band — instant-timing / 'no sooner / on the verge' set, 1 indexed + 2 redirects):
  か〜ないかのうちに (no sooner had ~ than; same verb twice Vる+か+Vない+かのうちに, second event arrives
  *before the first finishes* — tighter & more literary than たとたん; past-fact second clause, no commands;
  ↔ ta-totan instant-after-completion / ya-ina-ya literary-immediate / ka-to-omou-to surprise-contrast).
  **Folds (stay noindex):** かと思えば → **redirect → ka-to-omou-to** (ば-form variant of かと思うと/かと思ったら,
  + records そうかと思えば 'then again' contrast); もう少し/ちょっとで〜するところ(だった) → **redirect → tokoro-datta**
  (just the もう少しで/危うく 'nearly' adverb that 〜るところだった pairs with; ↔ sou-ni-naru). Anchored to
  enriched ta-totan/ya-ina-ya/ka-to-omou-to/tokoro-datta/sou-ni-naru. Clean build, lint clean (3), scan clean.
  · **batch 88** (uncommon band — 限{かぎ}り 'only/limit' family, 2 indexed): 〜限り/〜を限りに (the LIMIT 限り,
  reading-split from the enriched as-long-as conditional kagiri: N+限り 'only this once' 本日限り / N+を限りに
  'as of ~, ending' 今日を限りに / 声を限りに 'to the utmost'; ↔ kagiri conditional vs occasion-limit / dake-da
  everyday-only / kiri only-and-last) ↔ に限って ('of all ~', singles one case out with attitude — ironic bad
  luck 急いでいる時に限って or trusting denial うちの子に限って〜ない; ↔ ni-kagiru 'nothing beats' verdict / ni-kagirazu
  opposite-scope 'not limited to' / kagiri-2 occasion-limit). 限 homograph grid taught: 限り(as-long-as) vs
  限り/を限りに(only/cut-off) vs に限って(of-all) vs に限る(nothing-beats) vs に限らず(not-limited-to). kagiri-2
  conf med→high. **no-hoka-ni-nai already enriched as a redirect → skipped.** Anchored to enriched kagiri/
  dake-da/kiri/ni-kagiru/ni-kagirazu. Clean build, lint clean (2), scan clean.
  · **batch 89** (uncommon band — ところ-connective inference/situation set, 3 indexed; extends the batch-42/51
  ところ family): ところを見ると ('judging from', reads a *scene the speaker watches* → tentative guess, main
  clause MUST end らしい/だろう/に違いない; ↔ koto-kara fact-grounds firm / tokoro-kara source-trace / rashii
  the conjecture ending it pairs with) · ところから ('from the fact that / which is why', circumstance as the
  *source* a name/conclusion grew from — esp. how names arise 似ているところから〇〇と呼ばれる; ↔ koto-kara everyday
  near-syn / tokoro-o-miru-to scene-guess; **disambig from ところ+から-3 starting-point**) · ところを ('at a
  moment when / caught in the act', ところ as OBJECT of next verb — ①polite frame お忙しいところを、すみません
  ②caught-mid-action 逃げるところを捕まえた; ↔ tokoro-ni event *arrives* (intransitive) vs ところを verb *acts on*
  the scene (transitive) / ta-tokoro completion). tokoro-o conf med→high. Anchored to enriched koto-kara/
  tokoro-ni/ta-tokoro/rashii. **YAML trap caught:** inner `\"` double-quotes inside a double-quoted nuance
  string broke the build — strip nested double-quotes in prose (use single or none). Clean build after fix,
  lint clean (3), scan clean.
  · **batch 90** (uncommon band — volitional よう/まい modality set, 3 indexed): ようではないか ('let's ~',
  oratorical 〜ましょう upgrade — speeches/editorials rallying a group; casual ようじゃないか; ↔ dewa-nai-ka plain
  'isn't it?' on a statement vs exhortation on a volitional / volitional-form everyday よう) · ようか〜まいか
  ('whether to ~ or not', speaker wavering over their OWN action, feeds 迷う/悩む; ↔ ka-dou-ka yes/no-fact often
  someone-else's / mai negative-volition half / you-to-suru actually-attempting vs still-deciding) · ようと/
  ようが ('no matter ~/whatever', emphatic concession off volitional+と/が, pairs with question words 何が起ころうと,
  main clause unshaken; neg まいと/まいが; ↔ you-tomo も-emphasised sibling / te-mo basic-neutral 'even if' /
  you-ka-mai-ka deciding-vs-decided). you-to-ga conf med→high. Anchored to enriched dewa-nai-ka/volitional-form/
  mai/ka-dou-ka/you-to-suru/you-tomo/te-mo. **Slug traps:** かどうか = `ka-dou-ka` (not ka-douka); ではないか =
  `dewa-nai-ka`. Clean build, lint clean (3), scan clean.
  · **batch 91** (uncommon band — hearsay/quotation report set, 2 indexed + 1 redirect): との ('the ~ that',
  formal/written contraction of という that hangs reported content on a *communication/thought noun* 連絡/指示/
  見方 — news & business 中止との知らせ; ↔ to-iu spoken-neutral default / to-no-koto sentence-ending) ↔ とのこと
  ('I'm told that ~', polite relayed hearsay — business email/message-passing, speaker is the messenger not source;
  ↔ souda plain-hearsay / to-iu-koto-da hearsay+conclusion / to-no noun-modifying). **Fold:** とかで → **redirect →
  toka-2** (the 〜とか(で) 'vague reported reason' already covers it, example 急用ができたとかで). Anchored to enriched
  to-iu/souda/to-iu-koto-da/toka-2. **YAML/dup trap caught:** accidentally wrote two `formation:` keys in to-no
  (would die 'duplicated mapping key') — removed before build. Clean build, lint clean (3), scan clean.
  · **batch 92** (uncommon band — 次第 'as soon as / depending on' pair, 2 indexed): 次第 (**senses node**:
  ①Vます-stem+次第 'as soon as', formal, future-only — restriction: can't describe a past event, use たら/たとたん
  ②N+次第だ 'depends entirely on' 君の努力次第だ; +という次第だ 'this is how it came about' note; ↔ tara-sugu everyday
  as-soon-as past-or-future / ni-yoru neutral varies-by) ↔ 次第で ('depending on X the outcome varies', adverbial
  before a clause vs 次第だ predicate; 次第では 'depending on the case, might even ~' branch-flag; ↔ shidai predicate
  / ni-yotte neutral varies-by). shidai conf med→high. Anchored to enriched tara-sugu/ta-totan/ni-yoru/ni-yotte.
  Clean build, lint clean (2), scan clean.
  · **batch 93** (uncommon band — て-form determination / extreme-means pair, 2 indexed): てでも ('even by ~/
  even if it means ~', names an extreme *means* + strong-will second clause 借金してでも買いたい; ↔ te-mo general
  'even if' concession vs てでも extreme-means-offered / sae-ba minimum-condition opposite end of effort scale) ↔
  てみせる (**senses node**: ①'do ~ to demonstrate to someone' やってみせる ②'I'll definitely do ~, just watch'
  resolve 必ず合格してみせる; ↔ te-miru tentative-try-for-oneself inward vs てみせる outward demonstrate/vow /
  volitional-form plain-intention vs prove-to-audience). te-miseru conf med→high. Anchored to enriched te-mo/
  sae-ba/te-miru/volitional-form. Clean build, lint clean (2), scan clean.
  · **batch 94** (uncommon band — additive/escalating connective set, 3 indexed; extends enriched それに/その上/
  さらに/そして discourse web): さらには ('and even / moreover', escalating — the は marks the next item a step UP,
  caps a rising list 国内、さらにはアジア全域; ↔ sara-ni plain-furthermore/even-more / sono-ue comparable-extra) · なお
  ('note that / in addition', supplementary proviso opener for notices/documents なお、場所は変更; appends caveat NOT
  another argument; classical なお一層 note; ↔ sara-ni pile-on-point / sore-ni casual-besides) · それも ('and that too /
  at that', amplifies the SAME item with a striking detail それも新車を, often number+も fragment; ↔ sore-ni separate-
  new-point widens vs それも sharpens / sara-ni-wa escalate-to-broader-item). sore-mo conf med→high. Anchored to
  enriched sara-ni/sono-ue/sore-ni/soshite. Clean build, lint clean (3), scan clean.
  · **batch 95** (uncommon band — と-based relation/comparison connectives, 3 indexed): と並んで ('alongside /
  on a par with', ranks one thing at the same LEVEL/class 富士山と並んで; ↔ to-tomo-ni together-with/joint vs
  same-rank / to-onaji-kurai equal-degree vs same-rank) · と同じく ('the same as / likewise', adverbial 同じく
  modifying the FOLLOWING clause 去年と同じく今年も; ↔ to-onaji-de で-copula predicate-of-sameness vs く-adverbial /
  to-onaji-kurai equal-degree vs same-manner) · と逆に ('contrary to / the opposite of', polar reverse of a
  reference 予想と逆に, stronger than 'merely different'; とは逆に emph; ↔ hanmen two-sides-of-same-thing vs
  reverse-of-separate-ref / ni-taishite line-up-compare vs reverse). Anchored to enriched to-tomo-ni/to-onaji-de/
  to-onaji-kurai/hanmen/ni-taishite. **Slug note:** と違って/反対に have NO node — routed around. Clean build,
  lint clean (3), scan clean.
  · **batch 96** (uncommon band — temporal moment/way set, 2 indexed): 瞬間（に） ('the moment that', V-た+瞬間 —
  pinpoints the single instant + coincident event ドアを開けた瞬間冷気が; noun so refer-able その瞬間; ↔ ta-totan
  surprise-sequel vs neutral-pinpoint / tokoro-ni scene-broken-into / ka-nai-ka-no-uchi-ni before-first-finishes
  vs same-instant; **vs 一瞬 duration note**) · がけに ('on the way / just as ~ing', fixed motion-stem set
  出/帰り/行き/通り/寝 + incidental action 帰りがけに本屋に寄った; non-productive; ↔ tsuide-ni opportunity-of-main-task /
  nagara continuous-overlap). **sai (際) already a redirect → sai-ni → skipped.** Anchored to enriched ta-totan/
  tokoro-ni/ka-nai-ka-no-uchi-ni/tsuide-ni/nagara. Clean build, lint clean (2), scan clean. **Session b87–96:
  953 → 976 (+23 indexed + 5 redirects, 10 batches).**
  · **batch 97** (uncommon band — vague-listing particle set, 2 indexed + 1 redirect): やら (**senses node**:
  ①question-word+やら 'something or other' 何やら ②clause+ことやら/のやら 'I wonder / who knows' どうなることやら,
  pairs worry-verb; ↔ yara-yara paired-jumble / ka indefinite 何か neutral vs やら mystery-flavoured) ↔ 〜やら〜やら
  ('what with X and Y', chaotic/overwhelming pile-up or mixed emotions 嬉しいやら悲しいやら, takes V/A not just N;
  ↔ yara single-vague / ya neutral-noun-list / toka colourless-examples). **Fold:** 〜や〜や → **redirect → ya**
  (just the listing や repeated AやBやC). yara conf med→high, yara-yara med→high. Anchored to enriched ya/toka/ka.
  Clean build, lint clean (3), scan clean.
  · **batch 98** (uncommon band — それ-demonstrative connective pair, 2 indexed): それが ('actually / but against
  expectation', sentence-opener heralding a twist, esp. a reply overturning the question's assumption 「楽しかった?」
  「それが、雨で…」; **disambig from それ+が subject-marking**; ↔ tokoro-ga written-narrative-however / sore-nanoni
  'and yet' contradiction-of-two-facts) ↔ それは (**senses node**: ①'as for that' topic pick-up それは別の問題だ
  ②emphatic 'that's really ~' sympathetic reply それは大変でしたね, doubled それはそれは; ↔ sore-ga unexpected-twist /
  sore-ni adds-further-point). Both conf med→high. Anchored to enriched tokoro-ga/sore-nanoni/sore-ni. Clean build,
  lint clean (2), scan clean.
  · **batch 99** (uncommon band — 〜ものと assumption/presumption modality family, 5 indexed; dense N1 web):
  ものと思う ('assume / take for granted', もの = self-evident-default vs と思う personal-opinion) ↔ ものと思っていた
  ('had assumed (mistakenly)', past = belief now overturned, pairs てっきり; ↔ hazu-da reasoned-expectation) ↔
  ものと思われる ('it is presumed', impersonal passive objective inference for reports/news; ↔ mono-to-omou active /
  to-kangaerareru reasoned-conclusion) ↔ ものとする ('shall / it is stipulated', legal/contract decree; ↔ beki-da
  moral-should / mono-toshite assume-for-sake-of) ↔ ものとして ('on the assumption that / treating as', working
  premise for planning 来ないものとして計画; ↔ mono-to-suru stipulate-vs-suppose / to-shite real-role vs supposed).
  The 〜ものと grid: 思う(own-assume)/思っていた(mistaken-past)/思われる(impersonal-presume)/する(stipulate)/して(suppose).
  Anchored to enriched mono/to-omou/hazu-da/to-kangaerareru/beki-da/to-shite. **Slug traps:** hazu-datta/to-omotte-ita/
  to-sareteiru have NO node — routed to hazu-da/to-omou/to-kangaerareru. Clean build, lint clean (5), scan clean.
  · **batch 100** (uncommon band — 如何/いか- formal family, 4 indexed; dense N1 web): 如何（だ） ('the nature/state
  of ~ that an outcome hinges on', stiff/bureaucratic noun, base for いかんで/いかんにかかわらず; ↔ shidai everyday-formal-
  depends / ikan-de で-connective) ↔ いかんで（は） ('depending on ~', formal 次第で; いかんによって variant, polarity flip
  いかんによらず/にかかわらず='regardless'; ↔ shidai-de standard-register / ni-yotte neutral / ni-kakawarazu opposite-
  polarity) ↔ いかなる ('any/whatever ~', adnominal-before-NOUN formal どんな, +も='no exception'; ↔ donna everyday /
  donna-ni-temo concessive-before-verb) ↔ いかに (senses: ①'how (much) ~' degree exclamation/embedded-か ②いかに〜ても
  'however much ~' concession; ↔ dou everyday-how / donna-ni-temo spoken-concessive / ikanaru adverb-vs-adnominal;
  いかにも separate idiom). The 如何 grid: 如何だ(noun)/いかんで(depends)/いかなる(adnominal-any)/いかに(adverb-degree/concession).
  ikan conf med→high. Anchored to enriched shidai/shidai-de/ni-yotte/ni-kakawarazu/donna/donna-ni-temo/dou. Clean
  build, lint clean (4), scan clean. **Session b87–100: 953 → 989 (+36 indexed + 6 redirects, 14 batches).**
  · **batch 101** (uncommon band opener — formal scope/circumstance/concession connectives, 8 indexed + 1
  redirect): **topic/scope (に/は)** — に関係{かんけい}なく ('regardless of', result unaffected by the factor, plainer
  twin of にかかわらず ↔ ni-kakawarazu formal-written / o-towazu opens-category-to-all; low→high) · にかけては
  ('when it comes to ~ [unbeatable]', singles out a domain of excellence, main clause MUST be a confidence/
  superiority verdict — restriction ↔ ni-kakete the SPAN 'from~to~' completely different use of same shape /
  ni-totte importance-standpoint; low→high) · ついては (scoped to the **formal standalone connective** 'and so/
  to that end' — business letters, ties an established situation to the consequent request; variant つきましては;
  ↔ ni-tsuite everyday topic-marker について(は) which owns the 'as for ~' sense — kept distinct to avoid dup;
  med→high). **formal circumstance (の)** — の関係{かんけい}で ('due to/owing to', vague circumstantial reason ↔
  sei-de blame-bad-outcome / tame-da explicit-reason; high) · のもとで ('under [supervision/conditions]', sets
  authority one operates under ↔ ni-oite neutral-field; のもとに variant gathers-under-one-banner note; high).
  **concession** — とはいうものの ('that said / even so', calm reasoned concession granting prior truth ↔ to-wa-ie
  compact-literary-twin / mono-no clause-internal / noni emotional-reproach; med→high) · ことは〜が ('it's true
  that ~, but', repeated-word grudging concession VることはVるが/高いことは高いが; 〜には〜が variant note;
  **no confusable sibling node → contrasts empty by design** §6-B; low→high) · まだしも ('~ would be one thing,
  but', concedes a milder case to throw the worse one into relief, usually 〜ならまだしも; nara-madashimo N1 is the
  same construction → left for a future fold decision, noted not contrasted; high). **Fold:** の点{てん}で
  (no-ten-de) → **noindex redirect → ten-de** (点で's formation already covers Nの点で — true dup). Anchored to
  enriched ni-kakawarazu/o-towazu/ni-kakete/ni-totte/ni-tsuite/sei-de/tame-da/ni-oite/to-wa-ie/mono-no/noni/
  koto/ten-de. **NEW GOTCHA → §4:** `variants[]` `register:` must be an **array** (`["polite-spoken"]`), not a
  scalar — unlike most uses it mirrors the top-level `register` set; a scalar fails the build with
  "Expected array, received string" (caught at build, tsuite-wa). **Confidence bumps:** ni-kankei-naku/
  ni-kakete-wa/koto-wa-ga low→high, tsuite-wa/to-wa-iu-mono-no med→high. Clean build (after register fix),
  lint clean (9), scan clean. **Session batch 101: 989 → 997 (+8 indexed, grep 996).**
  · **batch 102** (uncommon band — ものなら conditional pair + "if it is the case" conditionals + formal
  "or"/"not only" listing, 7 indexed + 2 redirects; **crosses 1,000 indexed**): **ものなら pair** (taught as a
  potential-vs-volitional minimal pair) — ものなら ('if (by any chance) one could ~', V-potential + ものなら,
  wistful wish 帰{かえ}れるものなら帰りたい / dare できるものならやってみろ; ↔ you-mono-nara volitional-disaster /
  nara neutral-premise) ↔ （よ）うものなら ('if one were to ~, disaster follows', V-volitional + ものなら, small
  action→outsized bad consequence, written/emphatic; ↔ mono-nara; med→high). **"if it is the case" conditionals**
  — のであれば ('if it is the case that', formal explicit のなら, picks up a given premise ↔ nara everyday / ba
  general-condition) · ようでは ('if it is the case that [such a poor state], then [bad]', critical-tone,
  consequence must be NEGATIVE — restriction; ↔ youda plain-appearance / te-wa action-warning; med→high) ·
  たりしたら ('if (for example) ~', たり softens to one representative case, hedges a worry ↔ tara straightforward;
  〜たりすると note; たり has no node — routed to prose; med→high). **formal "or"/"not only"** — もしくは ('or',
  formal/written, forms & rules ↔ mata-wa default-neutral / aruiwa can-mean-perhaps / ka-2 spoken) · のみならず
  ('not only ~ but also', literary, のみ=formal だけ ↔ dake-de-wa-naku everyday / bakari-ka surprising-escalation).
  **Folds (stay noindex):** 〜も〜ば (mo-ba) → **redirect → mo-ba-mo** (front-half of the both-A-and-B frame) ·
  〜もし〜もする (mo-shi-mo) → **redirect → mo-ba-mo** (the する/し realization — mo-ba-mo's own example is
  歌も歌えば踊りもする). Anchored to enriched you-mono-nara/mono-nara/nara/ba/youda/te-wa/tara/mata-wa/aruiwa/
  ka-2/dake-de-wa-naku/bakari-ka/nomi/mo-ba-mo. **Confidence bumps:** you-mono-nara/youde-wa/tari-shitara med→
  high. Clean build, lint clean (9), scan clean. **Session b101–102: 989 → 1004 (+15 indexed, grep 1003). Milestone: 1,000 indexed crossed.**
  · **batch 103** (uncommon band — "worth / not worth / no need to" evaluative-modality web, 7 indexed +
  1 redirect; dense N2/N1 semantic cluster): **worth (positive pole)** — 甲斐{かい}がある ('worth the effort',
  V-た/Nの+甲斐がある, usually past 〜た甲斐があった = effort paid off ↔ kai-gai the 〜がい noun-suffix / ni-atai-suru
  objective-merit; 甲斐もなく negative note → kai-mo-naku) · に値{あたい}する ('worth/deserves/merits', objective
  verdict, 一読/賞賛に値する ↔ ni-taranai opposite-pole / ni-taeru passes-min-bar-vs-positively-deserves) · に
  耐{た}える (**2-sense** ①withstand/endure 高温に耐える ②be worth ~ing/hold-up-to-scrutiny 鑑賞に耐える, often neg
  読むに耐えない; ↔ ni-atai-suru; note: 〜の念に耐えない 'cannot suppress feeling' is a different fixed idiom; med→
  high). **not worth** — に足{た}らない ('not worth ~ing/insignificant', formal, fixed 取るに足らない; 〜に足りない
  variant + positive 〜に足る note; ↔ ni-atai-suru opposite / hodo-no-koto-wa-nai everyday-vs-formal) · ほどの
  ことはない ('not so much as to ~/no big deal', everyday, downplays the MATTER; absorbs the では variant; ↔
  ni-taranai / niwa-ataranai matter-vs-reaction; low→high). **no need to / doesn't warrant** — には及{およ}ばない
  (**2-sense** ①no need to V 心配するには及ばない, keigo-decline ②be no match for N 先輩には及ばない; ↔ niwa-ataranai
  action-vs-reaction) · には当{あ}たらない ('doesn't warrant [reaction]', REACTION/eval verb only 驚く・褒める・悲観する
  — restriction; ↔ ni-wa-oyobanai verb-type-giveaway / hodo-no-koto-wa-nai reaction-vs-matter). **Fold (stays
  noindex):** ほどのことではない (hodo-no-koto-dewa-nai N1) → **redirect → hodo-no-koto-wa-nai** (は/では variant —
  N2 は-form is canonical, lower JLPT). **ni-taru stays a stub** → referenced 〜に足る in prose, not contrast-linked.
  Anchored to enriched kai-gai/kai-mo-naku/ni-atai-suru/ni-taranai/ni-taeru/hodo-no-koto-wa-nai/niwa-ataranai/
  ni-wa-oyobanai. **Confidence bumps:** hodo-no-koto-wa-nai low→high, ni-taeru med→high. Clean build, lint clean
  (8), scan clean. **Session b101–103: 989 → 1011 (+22 indexed, grep 1010).**
  · **batch 104** (uncommon band — N1 concessive space, two tight sub-clusters, 9 indexed, no folds): **Cluster A
  — universal concessive "whether ~ or / no matter" (4):** だろうが／だろうと (N/な-adj + conjecture, sweeps a
  question word or paired list; restriction: with a VERB use volitional V-(よ)うが, not 〜だろうが; ↔ であれ formal
  twin / ようがまいが verb do-or-not / ても everyday) ↔ であれ (formal/written, NOUN/疑問詞 only, individualizes each
  value; restriction: not on verbs; ↔ だろうと colloquial twin / ようとも verb-version / にかかわらず neutral-vs-
  sweeping) ↔ ようが〜まいが (V-volitional + が + 同verb + まい + が, explicit do-or-don't binary; variant ようと〜
  まいと; ↔ ようとも single-intensified / だろうが noun-state / ても〜なくても everyday) ↔ ようとも (V-volitional/い-adj
  かろう/であろう + とも, emphatic-literary "even if/no matter how", often どんなに〜; ↔ you-to-ga plainer-twin / よう
  がまいが / ても). **Cluster B — "even so / nevertheless / and yet" contrastive connectives (5):** そうかといって
  (grants prior point then BLOCKS over-conclusion, pairs わけにはいかない/わけではない, leans negative; variant か
  といって; ↔ からといって reason-clause-bound / それでも pushes-through-vs-pulls-back / とはいえ compact-twin) · それ
  でいて ("and yet", two coexisting traits of the SAME subject, after て-form; restriction: same-subject not two
  events — use しかし; ↔ のに letdown-reproach / それでも one-event-despite) · しかしながら (formal/written しかし,
  no real restriction-slot by design; ↔ しかし register-pair THE contrast / とはいえ concedes-first) · もっとも-2
  (connective "though/mind you", partial reservation trails 〜が; **homograph note: ≠ 最も superlative / もっとも
  だ reasonable**; ↔ しかし full-reversal-vs-partial / ただし formal-proviso) · だろうに (modality; regret/reproach
  that counterfactual expectation didn't come true, after ば／たら, trails off; restriction: contrary-to-reality
  only; ↔ のに plain-contrary-fact / だろう neutral-conjecture-plus-contrastive-に). Anchored to enriched darou/
  de-aru/volitional-form/you-to-ga/shikashi/te-mo/noni/sore-demo/ni-kakawarazu/kara-to-itte/sore-de/datte +
  stub-but-exists targets to-wa-ie/tadashi/shikashi-nagara. **No folds.** Clean build, lint clean (9), scan
  clean. **Session b101–104: 989 → 1019 (+31 indexed, grep 1019).**
  · **batch 105** (uncommon band — N1, two tight sub-clusters, 7 indexed, no folds): **Cluster A — "tend to /
  apt to / liable to" (4):** ともすれば (adverb, latent usually-negative tendency, pairs 〜がち/〜やすい/〜かねない;
  restriction: general tendency not one-time ↔ ともすると と-twin / がち suffix-vs-adverb) ↔ ともすると (ば-twin,
  interchangeable ↔ ともすれば / どうかすると tendency-vs-occasional / がち) ↔ きらいがある (V-る/Nの + predicate
  'has a regrettable tendency', **negative-eval only** restriction 成功するきらいがある ✗ ↔ がち casual-recurrence-vs-
  formal-flaw / ともすれば adverb-vs-predicate / やすい neutral-prone) ↔ どうかすると (adverb 'sometimes / under
  certain conditions', pairs こともある/かもしれない/がち; **conf med→high** ↔ ともすると occasional-vs-tendency /
  かもしれない frequency-framing). **Cluster B — "as soon as / no sooner" temporal (3):** が早いか (V-る + literary
  'no sooner ~ than', stresses speed/abruptness, main clause past sudden action — restriction: no command/intent/
  state ↔ や否や neutral-twin / なり frozen-follow-on-state / たとたん everyday-unexpected) · そばから (V-る/た,
  **repeated futile cycle** 'as fast as ~ keeps undoing', restriction: repetition not one-off ↔ が早いか single-vs-
  recurring / たとたん one-time) · た弾みに (V-た + 'with the momentum of', **physical accidental result** restriction;
  variant 弾みで ↔ たとたん neutral-instant-vs-blames-momentum). Anchored to enriched gachi/yasui/kamoshirenai/
  ta-totan/nari/ya-ina-ya. **No folds.** Clean build, lint clean (7), scan clean. **Session b101–105: 989 → 1026
  (+38 indexed, grep 1026).**
  · **batch 106** (uncommon band — N1, three tight pairs, 5 indexed): **Cluster A — "covered in / full of / all"
  suffix triangle (2 + anchor だらけ):** まみれ (N + 'coated in a dirty substance' 泥/血/汗/油, always negative;
  restriction: a substance that clings, fig. limited to 借金まみれ ↔ だらけ scattered-countable / ずくめ composed-of) ↔
  ずくめ (N + 'entirely/nothing but', small fixed set 黒・いいこと・規則; **neutral-to-positive note** unlike まみれ/
  だらけ ↔ だらけ / まみれ). **Cluster B — "each / respectively" (2 + anchor それぞれ):** 銘々 (each person, formal-
  literary; restriction: people not things ↔ それぞれ everyday-all-purpose / 各々 near-syn) ↔ 各々 (each/respectively,
  formal-written, slightly broader; **conf low→high** — meaning standard, gate cleared ↔ 銘々 / それぞれ). **Cluster C
  — listing-example particle:** だの〜だの (lists grumbled examples with dismissive/annoyed tone, takes N/adj/V/quotes;
  restriction: negative-attitude not neutral ↔ や neutral-nouns / とか casual-neutral / なり〜なり choose-alternatives;
  **conf med→high**). **ya-ya (〜や〜や) left as the existing noindex redirect → ya** (already in redirect shape, thin
  by design — just listing や repeated). Anchored to enriched darake/sorezore/ya/toka/nari-nari. Clean build, lint
  clean (5), scan clean. **Session b101–106: 989 → 1031 (+43 indexed, grep 1031).**
  · **batch 107** (uncommon band — N1 に-particle "standard/basis" cluster + にまつわる, 4 indexed): the **"in
  accordance with / based on / in light of" web** (all off enriched ni-motozuite/ni-shitagatte/ni-sotte) —
  に即して (adapt action to *concrete reality/facts* 実情/現実/時代; restriction: concrete facts not abstract rule
  ↔ ni-nottotte rule-vs-reality / ni-terashite shape-to-fit-vs-judge-against / ni-motozuite) ↔ に照らして (evaluate
  a case *against a standard/law/precedent* 法律/経験/常識; restriction: yardstick-for-judgment ↔ ni-nottotte
  conform-vs-evaluate / ni-sokushite / ni-motozuite) ↔ に則って (*conform strictly to* an established rule/custom/
  ceremony 規則/伝統/前例; restriction: codified rule not facts/yardstick ↔ ni-shitagatte broad-follow-vs-formal-
  conform / ni-sokushite / ni-terashite) — the rule(則)/reality(即)/judge-against(照) three-way distinction is the
  GEO win. **にまつわる** (adnominal-only 'the tales/associations entangled around', storytelling flavour;
  restriction: must modify a noun, no adverbial *にまつわって話す ✗ ↔ ni-kanshite neutral-about / ni-tsuite plain-
  adverbial-ok / o-megutte contested-issue-vs-no-conflict). **Already noindex redirects — left as-is:** を中心に
  (→ o-chushin-to-ni-shite) and をめぐって (→ megutte-meguru) are pre-shaped redirect-hubs, not re-taught. **QA
  caught:** a Cyrillic phrase (связанные с) slipped into ni-matsuwaru's English example mid-write — fixed before
  scan; the Hangul+Cyrillic regex remains essential. Anchored to enriched ni-motozuite/ni-shitagatte/ni-sotte/
  ni-kanshite/ni-tsuite/o-megutte. Clean build, lint clean (4), scan clean. **Session b101–107: 989 → 1035 (+47
  indexed, grep 1035).**
  · **batch 108** (uncommon band — N1 "let alone / all the more / much more" escalation cluster, 4 indexed):
  the a-fortiori web — まして(や) (sentence-connective bridging two clauses, escalates a-fortiori from a baseline;
  restriction: needs a preceding statement ↔ はおろか one-clause-two-nouns / なおさら the-degree-adverb-it-introduces /
  どころか same-direction-vs-contradiction) ↔ はおろか (N + 'not even B, let alone A' both denied in ONE clause, 2nd
  noun takes も/さえ/すら + neg; restriction: negative clause; **conf low→high** ↔ ましてや two-clause / どころか stays-
  negative-vs-can-flip-positive) ↔ なおさら (degree adverb 'all the more' given an added reason, often the consequent
  of ましてや; ↔ さらに add-on-vs-intensify / にも増して benchmark-vs-reason) ↔ にも増して (N + 'more than [an already-
  high benchmark]', set phrase 何にも増して 'above all'; ↔ より everyday-vs-formal-surpass / なおさら). The はおろか
  negative-list vs ましてや two-clause-jump vs なおさら degree-adverb vs にも増して benchmark distinctions are the GEO
  win. Anchored to enriched dokoroka/sara-ni/yori. Clean build, lint clean (4), scan clean. **Session b101–108:
  989 → 1039 (+51 indexed, grep 1039).**
  · **batch 109** (uncommon band — N1 "as if to say / almost about to" ばかり-modality cluster, 3 indexed): とばかりに
  (quote/phrase + 'as if to say', message conveyed by manner not voiced; restriction: observable action ↔ to-iwan-
  bakari-ni explicit-言わん / n-bakari-ni different-ばかり-sense) ↔ と言わんばかりに (the **言う-instance of んばかり**, 'all
  but saying', 言わん = classical neg-volitional; ↔ to-bakari-ni shorter-form / n-bakari-ni 言う-vs-other-verb giveaway)
  ↔ んばかり(に) (V-ない-stem + 'almost on the verge of ~ing' vivid hyperbole, action does NOT occur, **する→せんばかり**;
  ↔ to-iwan-bakari-ni same-root-言う-becomes-idiom / kakeru nearly-begins-vs-actually-begun). The three split on: manner-
  message (とばかりに/と言わんばかりに) vs near-action hyperbole (んばかり), with と言わんばかりに the bridge (= 言う + んばかり).
  Anchored to enriched bakari/bakari-ni/bakari-da/kakeru. Clean build, lint clean (3), scan clean. **Session
  b101–109: 989 → 1042 (+54 indexed, grep 1042).**
  · **batch 110** (uncommon band — five formal-written clusters, 21 indexed, no folds): **Cluster A — formal
  additive/restatement connectives (6):** かつ (within-clause 'and also', stacks two parallel attributes of one
  thing 安全かつ確実; ↔ 及び set-membership-list / 並びに / そして sequence) · 並びに ('and', formal listing of nouns;
  及び joins items in the same small group, 並びに joins those groups — legal hierarchy; ↔ to-2 everyday / かつ
  attributes-vs-nouns) · ないし(は) (**senses**: ①'or' formal/legal = または ②'from~to~' numeric range 三ないし四日;
  ↔ mata-wa standard-or / aruiwa can-mean-perhaps) · すなわち ('namely', precise equivalent restatement 'i.e.';
  ↔ tsumari conversational-upshot / yousuru-ni summary-vs-equivalence) · 加えて ('in addition', sentence-opener
  separate-point; に加えて noun-bound note; ↔ sono-ue comparable / さらに also-raises-degree) · それゆえ ('therefore',
  literary consequence-opener pointing back; ↔ yue-ni bare-connector-mid-sentence / だから everyday / それで neutral-
  next-step). **Cluster B — 至る reach/extent (3):** に至る (reach/culminate in a grave endpoint 戦争に至る; に至っては/
  に至っても idioms + geographic-extent note; ↔ ta-sue effortful-outcome / に至るまで range-vs-endpoint) ↔ に至るまで
  ('all the way to / down to even', emphasises full reach incl. extreme member; ↔ made plain-endpoint / kara-ni-itaru-
  made both-ends) ↔ から〜に至るまで ('from A all the way to B', frames complete span, thoroughness; ↔ kara-made plain-
  span / に至るまで far-end-only). **Cluster C — を-connectives via/through/serving/starting/by-means (6):** を経て
  ('via/after passing through' a stage/place/time then moving on; 〜を経た adnominal; ↔ を通して whole-span-or-medium /
  てから plain-order) · を介して ('through an intermediary' person/org/medium 友人を介して/蚊を介して; ↔ を通じて heavy-
  overlap-medium / を通して sustained-channel) · を兼ねて ('serving also as', one act fulfils two set purposes 散歩を兼ねて;
  〜を兼ねた+N; ↔ がてら casual-incidental / かたがた formal-courtesy / ついでに opportunistic-extra) · を皮切りに ('starting
  with', first event launches expanding series, positive/dynamic; を皮切りとして variant; ↔ を経て pass-through-then-move-on /
  kara-3 plain-start) · をもって (**senses**: ①'by means of' formal/ceremonial 書面をもって ②'as of' boundary-time
  本日をもって閉店; これをもって set opener/closer; ↔ によって neutral-means / で everyday-instrumental) · をいいことに
  ('taking advantage of', exploits a circumstance unfairly, always disapproving; ↔ を機に neutral-seize-occasion-positive).
  **Cluster D — while-also/dual-purpose (3):** がてら ('while mainly ~ing, also ~', casual, motion-leaning, shared
  outing 散歩がてら; ↔ ついでに while-I'm-at-it / を兼ねて deliberate-two-purposes / ながら literally-simultaneous) ·
  かたがた ('while also', formal courteous secondary purpose, Sino-Japanese action noun, letters/visits お礼かたがた;
  ↔ がてら casual-motion / を兼ねて doubles-as / ついでに everyday) · ながらに ('while remaining in a state', literary,
  mostly fixed 涙ながらに/生まれながらに/昔ながら/居ながらにして; ↔ nagara simultaneous-actions / mama everyday-unchanged-
  state). **Cluster E — 'it's not as if' + emphatic label-denial (3):** ではあるまいし ('it's not as if', rejects an
  exaggerated premise → rebuke/advice, あるまい=formal neg-conjecture of ある; ↔ じゃあるまいし casual-twin / わけではない
  calm-conclusion-denial / まるで〜ようだ likening) ↔ じゃあるまいし (casual contraction, exasperated; ↔ ではあるまいし fuller /
  わけではない neutral) · でも何でもない ('not ~ in the least', emphatically denies a label is deserved 芸術でも何でもない;
  ↔ 全然〜ない plain-not-at-all / わけではない soft-conclusion-denial / まったく〜ない intensified-negative-vs-label-denial).
  Anchored to enriched oyobi/narabi-ni/katsu/soshite/to-2/mata-wa/aruiwa/tsumari/yousuru-ni/sono-ue/sara-ni/yue-ni/
  dakara/sore-de/ta-sue/made/kara-made/o-toshite/o-tsujite/te-kara/ni-yotte/de/o-ki-ni/tsuide-ni/nagara/mama/
  wake-de-wa-nai/marude-you-da/zenzen/mattaku. **Slug notes:** 'starting point' から = `kara-3`; をもって/ないし both
  taught as senses-nodes (boundary-time / range). All N1 (cluster A also-N1) formal-written band — no folds, no QA
  slips, lint clean (21), scan clean. **Session batch 110: 1042 → 1063 (+21 indexed, grep 1063).**
  · **batch 111** (uncommon band — three clusters: formal degree/extent adverbs + 済む resolution-modality +
  と "when it comes to / given that" connectives, 19 indexed, no folds): **Cluster 1 — formal degree/extent/
  manner adverbs (9):** 極めて (formal 'extremely', before adj/な-adj ↔ totemo everyday / かなり considerable-not-
  topmost) · さぞ (empathetic 'I can well imagine', about another's feelings, pairs でしょう; さぞかし emph ↔ きっと
  predict-outcome / だろう the-conjecture-itself) · 概ね (formal 'on the whole', broadly-true-minor-exceptions; **med→
  high** ↔ だいたい everyday / およそ rough-figure) · およそ (**senses** ①'roughly' figure ②'utterly' before neg-leaning,
  およそ〜ない ↔ だいたい / 概ね broadly-true) · 辛うじて ('barely/by a slim margin', positive-with-difficulty ↔ やっと
  relief-after-effort) · まるっきり (casual blunt 'completely/not-at-all', usu.+neg, no simile use ↔ まるで simile / 全然 /
  まったく its formal cousins) · ことごとく (literary 'every single one without exception', often adverse; note vs neutral
  全部/すべて — empty contrasts by §6-B) · たかが ('merely', belittles importance not just number; たかが〜されど idiom
  ↔ たった small-number / だけ neutral-limit / に過ぎない formal-deflate) · 強いて ('if pressed/forcibly', 強いて言えば ↔
  あえて dares-with-resolve vs forces-reluctantly). **Cluster 2 — 済む resolution-modality (5):** 済む (**senses** be-
  finished / be-settled-or-get-by-with で済む; **med→high** ↔ 終わる neutral-end vs settled-resolved / ずに済む fixed-
  pattern) · 済ませる (transitive twin 'get done / make do with' で済ませる; **low→high** ↔ 済む intransitive / 終わる) ·
  では済まない ('won't end with just', named response insufficient; 〜では済まされない stronger ↔ ずにはすまない can't-avoid-
  doing / て済むことではない て-form-grave-matter / どころではない rules-out-situation) ↔ ずにはすまない ('can't get away
  without ~ing', social/moral inevitability, する→せずに ↔ ざるを得ない broad-no-choice / なければならない neutral-must /
  ずに済む opposite) · て済むことではない ('~ alone won't settle it', moral rebuke ↔ では済まない noun-state / て済む
  affirmative-negated). **Cluster 3 — と "when it comes to / given that" (5):** ときたら (exasperated complaint-topic,
  familiar person/thing, casual ↔ となると hypothetical / ともなると notable-level / は neutral-topic; ったら lighter cousin) ·
  ともなると／となると ('once it reaches this notable level', consequence taken-for-granted; **med→high**; ともなれば
  variant ↔ となると plainer / になると literal-change / ときたら complaint) · とあって ('because, given a newsworthy
  circumstance', reportive/3rd-person ↔ から direct-reason / ので neutral-cause / とあっては conditional-twin) ↔ とあっては
  ('if such is the case → unavoidable obligation', main clause 〜ないわけにはいかない/ほかない ↔ とあって fact / とあれば
  willing-readiness / なら neutral) ↔ とあれば ('if it's for ~, I'd gladly', willing readiness; のためとあれば ↔ とあっては
  obligation / なら everyday / たら sequence). Anchored to enriched totemo/kanari/kitto/darou/daitai/yatto/marude/zenzen/
  mattaku/tatta/dake/ni-suginai/aete/owaru/zu-ni-sumu/te-sumu/zaru-o-enai/nakereba-naranai/dokoro-de-wa-nai/to-naru-to/
  ni-naru/wa/kara/node/nara/tara. **Missing-target notes (→ prose):** nantoka/subete/muri-ni/hobo absent — routed to
  yatto/全部-prose/aete/daitai. **Confidence bumps:** oomune/sumu med→high, sumaseru low→high, to-mo-naru-to med→high.
  No folds, no QA slips, lint clean (19), scan clean. **Session b110–111: 1042 → 1082 (+40 indexed, grep 1082).**
  · **batch 112** (uncommon band — four clusters: ならでは distinctive + 'if X, that brings its own issue' pair +
  に contrast/non-limitation + predicament/no-end modality, 11 indexed + 2 redirects): **Cluster A — ならでは
  distinctive (1 indexed + 2 redirects):** ならでは ('distinctive of / only possible for ~', always praising,
  ならではの+N most common ↔ だけあって result-fits-cause / こそ precisely) ← **ならではの (nara-de-wa-no) → noindex
  redirect → nara-dewa** (adnominal の slot) · **ならまだしも (nara-madashimo) → noindex redirect → madashimo**
  (なら+まだしも, the long-pending b101 fold resolved). **Cluster B — 'if X, that brings its own side' pair (2):**
  なら〜で ('if it's ~ then that too has its own side', repeats N/な-adj, resigned-accepting ↔ tara-tade verb/adj-past
  twin / なら single-premise) ↔ たら〜たで ('even once ~ turns out, that brings its own catch', repeats V/adj-past,
  〜ば〜で variant あればあったで ↔ nara-de noun-premise / たら straight-conditional). **Cluster C — に contrast/
  non-limitation (3):** にひきかえ ('in contrast to', subjective evaluative pairing of two DIFFERENT things; **med→
  high** ↔ に対して neutral-objective / 反面 same-thing-two-sides / に比べて degree-on-shared-scale) · に留まらず
  ('not limited to / spreads beyond', formal scope-extension ↔ だけでなく everyday / ばかりか surprising-escalation /
  に限らず opens-category) · によらず ('regardless of / not determined by', literary, 見かけによらず set-phrase + 'not
  relying on' sense ↔ にかかわらず everyday-variable / を問わず category-to-all / にもかかわらず fact-despite-concessive).
  **Cluster D — predicament/no-end modality (5):** 羽目になる ('end up stuck having to', unwelcome, often self-inflicted,
  V-る+ ↔ ことになる neutral-decision / 始末だ end-state) · 始末だ ('ends up in such a sorry state', deplorable
  end of bad chain, critical; この始末だ ↔ 羽目になる single-predicament / あげく(に) bad-result-of-process) · 切りがない
  ('there's no end to', no natural stopping point; note vs emotional たまらない — **contrasts empty §6-B**) · 術がない
  ('no way/means to', literary, 術もない emph ↔ 仕方がない resign-situation / よりほかない still-names-an-action) ·
  ないものか ('isn't there some way to ~?', earnest wistful wish, 〜ないものだろうか softer; **homograph note: ない+ものか
  yearning ≠ defiant rhetorical ものか b85** ↔ てほしい direct-want / だろうか wonders-fact). Anchored to enriched
  madashimo/dake-atte/koso/nara/tara/ni-taishite/hanmen/ippou-de/ni-kurabete/dake-de-wa-naku/bakari-ka/ni-kagirazu/
  ni-kakawarazu/o-towazu/ni-mo-kakawarazu/koto-ni-naru/ageku-ni/shikata-ga-nai/yori-hoka-nai/te-hoshii/darou-ka.
  **Redirect-hubs (stay noindex, sai.md-style — no foldInto, reappear in worklist by design):** nara-de-wa-no,
  nara-madashimo. **Missing-target notes (→ prose):** you-ga-nai/nai-darou-ka absent — routed to shikata-ga-nai/
  yori-hoka-nai/darou-ka. **Confidence bumps:** ni-hikikae med→high. No QA slips, lint clean (13), scan clean.
  **Session b110–112: 1042 → 1093 (+51 indexed, grep 1093).**
  · **batch 113** (uncommon band — two clusters: ても disclaimer/futility/intensity + 'it's about / practically'
  estimation-modality, 8 indexed): **Cluster A — ても disclaimer/futility/intensity (4):** て敵わない ('unbearably ~',
  negative-only unpleasant state, complaint tone; **disambig from かなわない 'no match for'** ↔ てたまらない pos-or-neg-
  intense / てしかたがない everyday-can't-help) · てもどうにもならない ('even if ~, nothing can be done', action futile
  because situation fixed ↔ どうにも just-can't / 仕方がない resign-situation / ても bare) · ても知らない ('do it & I'm
  not responsible', washing-hands warning, casual, closes よ/からね; **med→high** ↔ ても bare / と neutral-consequence) ·
  ても差し支えない ('it's fine even if', formal polite permission 'no objection/hindrance' ↔ てもいい everyday / てもかまわない
  I-don't-mind). **Cluster B — 'it's about / practically' estimation-modality (4):** といったところだ ('it's about / at most ~',
  modest estimate, pairs せいぜい ↔ というところだ near-syn written-vs-conversational / ぐらい bare-approx / せいぜい the-adverb)
  ↔ というところだ (near-syn, slightly more conversational; **disambig from literal というところ 'the point where'** ↔
  といったところだ / ぐらい) · くらいのものだ ('~ is about the only one', singles a lone case, often dismissive ↔ だけ neutral-
  limit / しかない plain-only / ぐらい) · も同然だ ('practically / as good as ~', falls just short but amounts to it, N/V-た+;
  〜ようなものだ near-equiv prose ↔ と同じくらい equal-degree / ぐらい approx). Anchored to enriched te-tamaranai/
  te-shikata-ga-nai/dou-nimo/shikata-ga-nai/te-mo/te-mo-ii/temo-kamawanai/to-conditional/gurai/seizei/dake/shika-nai/
  to-onaji-kurai. **Missing-target notes (→ prose):** ni-hitoshii/you-na-mono-da absent — 〜ようなものだ noted in prose
  on mo-douzen-da. **Confidence bump:** temo-shiranai med→high. No folds, no QA slips, lint clean (8), scan clean.
  **Session b110–113: 1042 → 1101 (+59 indexed, grep 1101).**
  · **batch 114** (uncommon band — five clusters: without/missed-chance + counterfactual/pretense +
  limit-unreasonable-never + expressive estimation + temporal ever-since, 26 indexed): **A — without /
  failed / missed chance (8):** ことなしに (written 'without ~ing', frames X as a necessary means, は→neg
  main clause ↔ koto-naku just-without / zu-ni everyday / nashi-ni noun-based) · もしないで (emphatic
  'without even ~ing', reproach; も splits the verb 見もしない/確認もしない ↔ nai-de neutral / zu-ni plain) ·
  ないでも (concessive 'even without ~ing' ↔ nakute-mo standard / nai-de) · ともなく (**senses**: ①aimless
  見るともなく見る ②vague-source どこからともなく ↔ to-mo-nashi-ni) ↔ ともなしに (literary twin, aimless-only,
  no vague-source use; **med→high** ↔ to-mo-naku) · ずじまい (ended up never ~ing, regret/finality,
  する→せず ↔ sobireru miss-timing / zu-ni plain) · そびれる (miss the chance/timing, hesitation 言いそびれる
  ↔ sokonau broad / zu-jimai resulting-state) · 損{そこ}なう (**senses**: fail-to-do / do-wrongly 書き損なう;
  死に損なう 'narrowly' note; 損ねる variant ↔ sobireru timing-only). **B — counterfactual/pretense (5):**
  たら〜ところだ (counterfactual narrow-miss 'would have but didn't', result=ところだった, pairs 危うく/もう少しで
  ↔ tokoro-datta bare / sou-ni-naru involuntary) · たところで (concessive futility 'even if ~, useless',
  neg/pointless main clause, た≠past ↔ te-mo neutral / **ta-tokoro aspect homograph**; ところで 'by the way'
  note) · たことにする (chosen fiction 'pretend ~ (didn't) happen', retroactive; **med→high** ↔ furi-o-suru
  act-out / koto-ni-suru tense-flips-decision-vs-fiction / ka-no-you-da observer-simile) · たつもりはない
  (deny intent/deed 'didn't mean to / no sense of having ~ed' ↔ tsumori-datta had-intended / tsumori) ·
  たくても〜ない (thwarted desire 'can't even if want to', same-verb potential-neg, external blocker;
  **med→high** ↔ you-ni-mo-nai thwarted-attempt / te-mo). **C — limit/unreasonable/never (5):** にもほどがある
  (indignant rebuke 'there's a limit to', nuance fires ↔ sugiru neutral-excess) · には無理がある (flaw/stretch
  'unreasonable'; vs 無理だ 'impossible' note; contrasts empty §6-B) · ためしがない (never-once track-record,
  critical; vs ことがない neutral note — no node) · 限{かぎ}りだ (peak emotion 'couldn't be more ~', emotion-adj
  only ↔ **kagiri conditional homograph** / to-ittara-nai colloquial-peak) · 心配がある (personal worry/risk;
  **med→high** ↔ osore-ga-aru formal-forecast / kanousei-ga-aru neutral). **D — expressive estimation (5):**
  といおうか (groping for the word 'or should I say', often doubled AといおうかB ↔ to-iu-yori decisive-replace /
  mushiro commits) · と言えなくもない (cautious double-neg 'one could even say', hedges a judgment ↔ to-ieru
  affirmative / nai-koto-mo-nai hedges-action) · といったらない (indescribably ~, colloquial peak of any
  emotion; ありゃしない/ったらない variants ↔ kagiri-da composed-written; **vs といったところだ estimation note**) ·
  とは比べものにならない (different league, comparison meaningless ↔ yori ranks-on-scale / to-onaji-kurai antonym) ·
  たとえて言えば (announce an analogy, pairs ようだ ↔ iwaba direct-label). **E — temporal (3):** てからというもの
  (emphatic 'ever since', lasting change/habit, no one-off ↔ te-kara neutral-after / irai matter-of-fact-span) ·
  たら最後 (irreversible bad result 'once you ~, no going back', beyond-control; たが最後 variant ↔ tara neutral) ·
  たなり (literary 'left just as ~, nothing more', neglect/prolonged ↔ mama everyday / kiri たきり spoken-twin;
  **vs as-soon-as なり homograph note**; **med→high**). **Confidence bumps:** to-mo-nashi-ni/ta-koto-ni-suru/
  takute-mo-nai/shinpai-ga-aru/ta-nari-de med→high. **Seed-title fix:** tara-saigo (unclosed paren).
  **Slug notes:** koto-ga-nai/ta-koto-ga-aru/te-irai/sokoneru absent — routed to notes/variants. No folds,
  no QA slips, lint clean (26), scan clean. **Session batch 114: 1101 → 1127 (+26 indexed, grep 1127).**
  · **batch 115** (uncommon band — three clusters: quality-acquisition suffixes + emphatic negation adverbs +
  expectation/impulse/retrospection adverbs, 14 indexed + 1 redirect): **A — quality-acquisition suffixes (4):**
  〜びる (Noun+びる→ichidan, natural/gradual quality often via age/wear 古{ふる}びる/大人{おとな}びる, involuntary ↔
  buru deliberate-pose / meku touch-of / ppoi everyday-ish) · 〜ぶる (Noun/な-adj+ぶる→godan, deliberate phony pose
  偉{えら}ぶる/知{し}ったかぶる, critical; restriction: implies pretense ↔ biru natural-acquire / furi-o-suru
  one-off-pretend / garu shows-real-feeling) · 〜めく (Noun+めく→godan, 'show signs of/a touch of' 春{はる}めく/
  謎{なぞ}めく, literary, adnominal めいた ↔ biru fully-acquire / jimita negative-vs-atmospheric) · 〜じみた
  (Noun+じみた, NEGATIVE 'unbecomingly tinged with' 子供{こども}じみた/所帯{しょたい}じみた; restriction: negative-only
  ↔ ppoi neutral-ish / meku atmospheric / buru deliberate-pose; from 染{じ}みる). **B — emphatic negation adverbs
  (4 indexed + 1 redirect):** 何ら〜ない (formal categorical 'not any whatsoever', abstract nouns; **med→high**; 何らの
  variant ↔ mattaku everyday / sukoshi-mo degree) · とうてい〜ない (到底, 'cannot possibly, no effort suffices';
  **med→high**; neg-bound restriction ↔ totemo〜ない near-syn-everyday / zenzen degree-zero) · あながち〜ない ('not
  necessarily/entirely', concedes partial truth, fixed neg endings ↔ to-wa-kagiranai predicate-vs-adverb; 必ずしも
  prose) · 〜として〜ない (一+counter+として+neg 'not even one' 一日{いちにち}として; **med→high**; restriction: 一 fixed
  ↔ sukoshi-mo degree / nanra-nai abstract-vs-counted) ← **一〜として〜ない (ichi-to-shite-nai) → noindex redirect →
  to-shite-nai** (same construction, 一 obligatory). **C — expectation/impulse/retrospection adverbs (6):** 案の定
  ('sure enough, as feared', predicted bad outcome confirmed ↔ yahari neutral-good-or-bad / hatashite formal+question)
  · 果たして (**senses** ①'sure enough' confirm-prediction ②'(really?)' opens doubtful question 〜だろうか ↔ an-no-jo
  feared-only / yahari everyday) · 思わず ('involuntarily/reflexively', reflex to stimulus +てしまう; restriction:
  unintended ↔ tsui lapse-against-judgment / ukkari careless-mistake) · 思い切って ('boldly / take the plunge',
  overcome own hesitation ↔ aete dare-hard-option-on-purpose / omowazu deliberate-vs-reflex) · 思えば ('looking
  back / now that I think of it', retrospective opener 今思えば; **med→high**; ば-conditional of 思う, no confusable
  sibling → contrasts empty §6-B) · 見るからに ('visibly/obviously at a glance', from appearance +そうな; restriction:
  visible-only ↔ ikanimo fits-stereotype / akiraka-ni any-evidence-incl-reasoning). **Confidence bumps:** nanra-nai/
  toutei-nai/to-shite-nai/omoeba/ichi-to-shite-nai med-or-low→high. **Missing-target notes (→ prose):** 必ずしも
  (kanarazushimo-nai)/hitotsu-mo-nai/kangaete-mireba absent. No QA slips, lint clean (15), scan clean. **Session
  batch 115: 1127 → 1141 (+14 indexed, grep 1141).**
  · **batch 116** (uncommon band — four clusters: enumeration openers + hypothesis/whether + formal occasion +
  そこを/にして particles, 9 indexed + 1 redirect): **A — enumeration 'for one thing / on one hand' (4):** 第一{だいいち}
  ('first of all / for one thing', foregrounds foremost point, also 'above all'; **med→high** ↔ hitotsu-ni-wa
  one-of-several) · 一つ (**senses** ①'for one thing' point-marker ②softener '(just/kindly) ~' ひとつよろしく/やってみよう;
  **low→med + review_reason** ↔ hitotsu-ni-wa crystallized-connective) · 一つには ('for one thing, one reason being',
  explicit enumeration, pairs 二つには; **med→high** ↔ daiichi ranking / hitotsu softener) · 一方では〜他方では〜
  (balances two coexisting sides, formal; **med→high** ↔ ippou-de single-add / hanmen same-thing-two-sides).
  **B — hypothesis/whether (2):** 仮に ('supposing/hypothetically', premise-as-not-real, pairs 〜としたら/〜としても ↔
  moshi-mo real-if / tatoe-temo concessive) · 〜か否か (formal/written 'whether or not', 否=classical no ↔ ka-dou-ka
  everyday / ka-ka two-named-alternatives). **C — formal occasion (1 + 1 redirect):** 節に ('on the occasion of',
  polite correspondence set-phrase その節は; **med→high** ↔ ori warm-general / sai-ni neutral-official) ← **折には
  (ori-niwa) → noindex redirect → ori** (は-marked form; ori already covers 折に/折には). **D — particles (2):** そこを
  ('despite that / I-know-but', plea to override a stated obstacle, そこを何とか/曲げて; **med→high** ↔ noni neutral-
  although) · 〜にして (**senses** ①'at/even at a stage/age' 六十にして/この年にして初めて ②'in an instant' 一瞬にして/
  一夜にして ↔ sae extreme-example-vs-point-on-scale; 今にして思えば note). **o-4 (emotive を) DEFERRED:** ものを already
  enriched as mono-o; bare emotive を obscure/low-conf → left for a rare-particle pass. Anchored to enriched
  ippou-de/hanmen/moshi-mo/tatoe-temo/ka-dou-ka/ka-ka/ori/sai-ni/noni/sae. No QA slips, lint clean (10), scan clean.
  **Session b115–116: 1127 → 1150 (+23 indexed, grep 1150).**
  · **batch 117** (uncommon band — three adverbial clusters: evaluative/manner adverbs + temporal-stance
  adverbs + emotion/reference/degree adverbials, 14 indexed): **A — evaluative/manner adverbs (5):** いかにも
  ('every bit the ~ / just like a typical ~' + intensifier 'truly', pairs 〜らしい/〜そう; standalone 'indeed'
  agreement note ↔ miru-kara-ni visible-at-a-glance-vs-fits-stereotype) · あくまでも (**senses** ①persist-to-the-
  end ②strictly/merely-qualify 個人的意見; variant あくまで ↔ doko-made-mo limitless-extent-vs-unwavering-stance) ·
  中途半端 (な/に 'halfway/half-hearted', almost-always-negative; **conf med→high**; no confusable sibling →
  contrasts empty §6-B) · 下手に ('rashly/ill-advisedly → backfires', pairs と/ば+bad-result; **restriction:
  not the plain adverb of 下手 skill**; **med→high**; contrasts empty) · それなりに ('in its own way/reasonably',
  fixed pronoun-phrase ↔ nari-ni noun-attached-whose-own-way; それなりの+N note). **B — temporal-stance adverbs
  (3):** 今更 ('now of all times / too late', pairs ても/neg/rhetorical-Q; restriction: not neutral 'now';
  今更ながら set-phrase) · 一旦 (**senses** ①'once ~ → inevitable consequence' +たら/と ②'for the time being'
  中断; 一度 count-vs-turning-point note) · 依然(として) ('still/as before, unchanged', formal/written ↔ speech
  相変わらず/まだ; variant 依然 drops として). **C — emotion/reference/degree (6):** ことに ('to one's surprise/
  joy/regret', emotion-word-fronted; **restriction: emotion/eval words only** ×高いことに; prereq koto) · 割合
  ('comparatively/fairly', plain adverb; **conf med→high**; variant 割合に ↔ wari-ni-wa against-a-stated-yardstick;
  prereq wari-ni-wa; **vs noun 割合 'ratio'**) · ただの ('a mere/just a ~', NOUN-attach restriction vs adverb ただ ↔
  tada adverb-merely / dake quantity-vs-quality-downplay) · 例の ('that ~ we both know', shared-knowledge/discreet;
  例のごとく 'as usual' note) · そのもの ('the very ~ / embodiment of', N/な-adj-stem; **conf med→high** ↔ jitai
  singles-out-to-evaluate-vs-intensify-embodiment) · 僅か ('only/a mere/slight', number/amount/degree; **conf med→
  high** ↔ wazuka-ni adverb-slightly / tatta number-only-vs-broader-formal). Anchored to enriched miru-kara-ni/
  doko-made-mo/nari-ni/koto/wari-ni-wa/tada/dake/jitai/wazuka-ni/tatta. **Confidence bumps:** chuto-hanpa/hetani/
  wariai/sono-mono/wazuka med→high. **Fix caught mid-write:** dropped a mismatched ittan↔ichido-ni contrast
  (一度に = 'all at once', not 一度 'one time') → moved the 一度 distinction to a note. Clean build, lint clean (14),
  scan clean. **Session batch 117: 1150 → 1164 (+14 indexed, grep 1164).**
  · **batch 118** (uncommon band — five clusters: こと-reason connectives + parity/extent suffixes +
  listing/aside connectives + dependency/concession conditionals + effort-in-vain, 14 indexed): **A —
  こと-connectives (3):** ことだし ('since ~ among other things', soft justification → decision/suggestion ↔
  koto-dakara predict-from-character / shi plain-reason-stack) · こともあって ('partly because ~', one factor
  behind an already-arisen result ↔ koto-dashi leads-to-decision / sei-de pins-one-bad-cause) · ことのないように
  (emphatic negative purpose 'so that ~ never happens' ↔ youni general-purpose / koto-naku without-doing).
  **B — parity/extent suffixes (3):** 並み ('on a par with / up to ~ level', compact N-suffix ↔ to-onaji-kurai
  roughly-equal-degree; 人並み/軒並み fixed-forms note) · ぐるみ ('the whole ~ together / ~-wide', group-noun-only
  restriction 家族/会社/町 ↔ no sibling §6-B; collective-wrongdoing note) · 来〔らい〕 ('for the past ~', span-suffix
  continuing-to-now; **conf low→high** ↔ irai ever-since-an-event vs duration-suffix; 本来/従来/将来 fixed-vocab
  note). **C — listing/aside connectives (3):** といい〜といい ('what with A and B alike', two facets → one
  evaluation; **conf med→high** ↔ mo-mo plain-add / ni-shiro-ni-shiro concessive-choice-vs-supporting-evidence) ·
  と相まって ('coupled with ~', two factors interact→amplify, formal ↔ ni-kuwaete merely-adds / to-tomo-ni
  together-with) · はさておき ('setting ~ aside → to the main point'; **conf med→high** ↔ wa-tomokaku conversational-
  dismissive / wa-betsu-to-shite neutral-deferral). **D — dependency/concession (3):** あっての ('the A that only
  B makes possible', N1あってのN2 ↔ nakushite-wa negative-condition-clause / nashi-ni-wa without-before-verb;
  命あっての物種 proverb) · なくして(は) ('without ~, there can be no ~', formal, negative/impossible main clause
  ↔ nashi-ni-wa everyday / nai-koto-ni-wa verb-clause-unless) · ないまでも ('even if not ~, at least ~', concedes
  bigger-action-won't-happen + asserts lesser, set frame 〜とは言わないまでも ↔ nakute-mo even-without). **E —
  effort-in-vain (1):** 甲斐もなく ('despite ~, to no avail', disappointing outcome ↔ kai-ga-aru paid-off-opposite /
  kai-gai 〜がい worthwhile-suffix). Anchored to enriched koto-dakara/shi/youni/koto-naku/to-onaji-kurai/irai/mo-mo/
  ni-shiro-ni-shiro/ni-kuwaete/to-tomo-ni/wa-tomokaku/wa-betsu-to-shite/nashi-ni-wa/nai-koto-ni-wa/nakute-mo/
  hou-ga-mashi-da/yori/kai-ga-aru/kai-gai/sei-de. **Confidence bumps:** rai low→high; to-ii-to-ii/wa-sate-oki
  med→high. **Missing-target notes (→ avoided):** nai-youni-suru/dano-dano/to-mo absent — routed to youni/
  ni-shiro-ni-shiro/mo-mo. Clean build, lint clean (14), scan clean. **Session b117–118: 1150 → 1178
  (+28 indexed).**
  · **batch 119** (uncommon band — four clusters: surprise-contrast & scope-denial + number/composition
  particles + sentence-final particles/registers + condition/dual-nature/warning, 14 indexed): **A —
  surprise/scope-denial (4):** かと思いきや ('just when one thought ~, contrary to expectation', literary,
  surprise-reversal ↔ ka-to-omou-to quick-succession-vs-contradicted-expectation; 思いきや old 思う+や note) ·
  全ては〜ない ('not all', は-partial-negation; **conf med→high**; restriction: は essential, without it = total
  denial ↔ zenbu-wa-nai everyday-twin) · に限ったことではない (sentence-final verdict 'not limited to just ~,
  applies widely' ↔ ni-kagirazu mid-sentence-category-opener / ni-kagitte singles-out-with-attitude opposite-job)
  · どころの話ではない ('far from it / out of the question', emphatic, grave-reality-dismisses-trivial; **conf med→
  high** ↔ dokoro-de-wa-nai base-form / dokoroka reverses-to-opposite). **B — number/composition particles (3):**
  からある ('as much/many as / no less than', large-figure emphasis, からする prices/からいる people ↔ mo-2 everyday-
  number-も) · からなる ('consist of / composed of', structured-whole components, formal ↔ de-dekiru physical-
  material-vs-constituent-parts; よりなる literary note) · 単位で ('by units of / per ~'; **conf med→high** ↔ goto-ni
  every-each-vs-unit-of-measure). **C — sentence-final particles/registers (4):** たまえ (man's gentle command to
  inferior, dated/fiction, Vます-stem ↔ nasai gender-neutral-parent-teacher / imperative blunt; from 給う) · とも
  ('of course/certainly', emphatic affirmative answer; **conf med→high** ↔ yo informs-vs-confirms; disambig from
  concessive 〜とも 'even if' & quotative) · わ (soft feminine sentence-final emphasis, inward-feeling; **title fix**
  truncated→full ↔ yo asserts-outward / ne seeks-agreement; Kansai-male falling-tone わ note) · ときに ('by the way',
  formal/dated topic-break, often polite enquiry; **conf med→high** ↔ tokoro-de everyday / sate own-agenda-next;
  disambig from 〜ときに 'when'). **D — condition/dual-nature/warning (3):** ようによっては ('depending on how/the
  manner', V-stem+よう+によっては ↔ you base-noun-way / shidai-de depends-on-factor-vs-manner; often +も) · でもあり
  〜でもある ('is both A and B at once', two coexisting/paradoxical identities of one subject ↔ de-mo-aru single-
  also / mo-mo lists-items-vs-assigns-identities) · さもないと ('otherwise / or else', standalone warning after
  command, さもなければ/さもなくば variants ↔ de-nai-to condition-bound / nakereba neutral-negative-conditional).
  Anchored to enriched ka-to-omou-to/zenbu-wa-nai/ni-kagirazu/ni-kagitte/dokoro-de-wa-nai/dokoroka/mo-2/de-dekiru/
  goto-ni/nasai/imperative/yo/ne/tokoro-de/sate/you/shidai-de/de-mo-aru/mo-mo/de-nai-to/nakereba. **Confidence
  bumps:** subete-wa-nai/dokoro-no-hanashi-de-wa-nai/tani-de/tomo/toki-ni med→high. **Seed-title fix:** wa-3
  (truncated 'feminine spee'). **Quote-safety:** rewrote tomo's dialogue key sentence with single quotes (no
  nested double-quotes). Clean build, lint clean (14), scan clean. **Session b117–119: 1150 → 1192 (+42 indexed).**
  modality する/なる oppositions, keigo & こそあど register ladders, benefactive viewpoint mirrors,
  connective result/concession/condition axes.
- **`common` band DRAINED (batch 72).** All remaining `--freq common` stubs are resolved noindex
  redirect-hubs (folds from batches 12/15/19/21/35/36/37/40/42/58/60/61/62/66/68) that reappear in
  the worklist by design — skip them. **Next batch = `--freq uncommon`.** Run
  `python3 scripts/list_stubs.py --freq uncommon` (then `rare`). The historical common-band notes below
  are kept for reference. Modality + keigo + こそあど + benefactives +
  basic connectives + aspect/causative/passive + quotation/nominalizers + conditionals + だけ/ばかり
  limitation + 以外/ほか exclusion + person/address suffixes + change-of-state する/なる + sensation
  がする + emotion-display + する-inference connectives + contrast/result/"speaking-of"/concessive-からといって
  connective web (batch 36) largely mined; remaining good families:
  **degree/extent adverbials** (donnani/doushitemo/dou-ka/goto-ni/gimi/darake/buri-ni), the
  **〜を通して/〜を通じて means/perspective particles** (o-toshite + siblings), the **〜たって/〜ったって
  concessive-colloquial set**, or the **〜ことから/〜ことだから reason-from-grounds connectives**. **Heads-up:** the redirect-hubs — batch-15's dake-de-wa-naku-2, bakari-de-wa-naku,
  bakari-de-wa-naku-2, bakari-de-wa-naku-4, igai-wa; batch-19's ni-tsuite-wa, baai-wa, no-baai-wa;
  batch-21's wa-iu-made-mo-nai — stay `noindex:true` by design and will **reappear in the worklist** — they're resolved redirects to a
  canonical, not pending work (same as batch-12's chau/chimau/toku). Skip them. Note: two unresolved
  near-dup stub pairs still need a catalog-level fold decision — `o-suru`(N3)/`o-suru-2`(N4) and
  `yaru`/`yaru-3`/`te-yaru`.
  **Process (user directive 2026-06-15, throughput revised 2026-06-19):** roll multiple clusters
  back-to-back per turn, then ONE consolidated build; checkpoint PASS + HISTORY once per turn, not
  per cluster. **Context can safely run to ~20% (1/5) per turn — that is the target ceiling.**
  Reference point: ~40+ nodes (4 clusters) lands context at only ~13%, so ~20% is roughly 60–70
  nodes / 5–6 clusters in a turn. Don't stop at one ~15-node batch. A consolidated build + checkpoint
  per cluster-group is fine (batch 12 then 13 each got their own build in one turn); the cap is the
  20% context line, not a node count.
  **The 20% ceiling is MY responsibility to check, not a hook's (user directive 2026-06-19).**
  "Keep rolling" does NOT mean "never come up for air." Between clusters — at each build+checkpoint
  boundary — I explicitly check context usage against the ~20% line myself and decide whether to
  start another cluster-group or stop. And I **actually yield the turn** after each build+checkpoint
  (end the turn / hand control back) rather than chaining indefinitely, so the harness hook can
  re-sample fresh state (context %, file changes, any injected guidance) before the next group
  begins. The pattern is: cluster(s) → build → checkpoint (PASS+HISTORY) → **yield**; on the next
  turn, re-check the threshold and continue. A yield between groups is the norm, not an exception —
  it is cheap insurance against drifting past the ceiling or acting on stale state.
  **Watch:** `variants[]` schema is `form:` (+ optional `note:`/`reading:`/`register:`), NOT
  `text:` — using `text:` fails the build (caught batch 6). A pure prose aside with no
  alternate form belongs in `notes:`, not `variants:`.
- There is **no cursor file** — `list_stubs.py` *is* the resume state (a node is done iff
  `noindex:false`). `--enriched` lists finished nodes. `foldInto` nodes are excluded by
  default (folded forms aren't pending work; `--include-folds` to see them).
