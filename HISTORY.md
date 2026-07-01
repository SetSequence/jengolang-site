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
