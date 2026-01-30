setcps(110/60/4)

// Ocarina sparkle
$: note("~ d5 e5 ~ a5")
  .s("ocarina").gain(0.12).lpf(1200).slow(6)
  .legato(1.2).scope().size(4).color("cyan")

// Clarinet melody
$: note("d4 e4 f#4 a4 [f#4*2 e4] d4 a3")
  .s("clarinet").legato(1.4).gain(0.33)
  .room(0.45).lpf(1200).slow(2.5).rev()
  .sometimes(x => x.add(0.02)).color("magenta")

//Add the harps
$: note("d4 a4 f#4 a4 [d4 d4*2] a4 f#4 a4")
  .s("harp").gain(0.5).legato(0.9)
  .room(0.45).slow(3)

// bagpipes drone
$: stack(
  note("d2").s("triangle").gain(0.22).slow(8),
  note("d2").s("triangle").gain(0.15).slow(8),
  note("d2").s("triangle").gain(0.18).slow(8)
).legato(1.7).room(0.6).lpf(300).gain(seq(0.6, .9).slow(12))
  .scope().size(1.5).color("<green yellow>")


// ornamental layer
$: note("~ d4 f#4 g4*2 ~ a4")
  .s("ocarina").gain(0.15)
  .legato(0.4).room(0.5)
  .sometimes(x => x.fast(2))
  .sometimes(x =>x.add(12)).slow(6)

// wind through grass
$: s("noise").gain(seq(0.054, 0.09, 0.06).slow(18))
  .lpf(1000).room(0.8).sometimes( x => x.fast(1.5))
