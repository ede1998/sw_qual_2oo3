use std::env;

fn reliaele(lambdai : f64, t : f64) -> f64 {
    (-(-lambdai*t).exp()).ln_1p()
}

fn reliareduce(elems : &mut std::iter::Iterator<Item = f64>, t : f64) -> f64 {
    -elems.map(|e| reliaele(e, t)).sum::<f64>().exp_m1()
}

fn main() {
    let a = reliareduce(&mut env::args().skip(1)
                        .map(|s| s.parse::<f64>().expect("NAN?")), 87600f64);
    println!("{:e}", a);
}
