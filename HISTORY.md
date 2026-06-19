# HISTORY — Grammar skill-tree build log (archived from TREE.md)

Append-only. Not needed for forward work — the live cursor is `PASS.md`,
the design is `TREE.md`. Kept for provenance / debugging a past decision.

---

## Pass-2 dated build log

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
