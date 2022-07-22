use std::io;
use std::time::{Duration, Instant}; // NOTE: This is only used for benchmarking

// Simple looping algorithm
fn factorial_loop(mut f: i64) -> i64 {
    // sum is 1 so if f is 0 the function returns 1
    let mut sum: i64 = 1;

    // Multiplying the sum by f and subtracting f by 1 every loop
    while f > 0 {
        sum *= f;
        f -= 1;
    }

    return sum;
}

// Recursive algorithm
fn factorial_recursion(f: i64) -> i64 {
    // Return 1 if f is 0 otherwise we multiply the current f by
    // the result of our current function f-1
    return if f <= 0 { 1 } else { f * factorial_recursion(f-1) }
}

fn main() {
    println!("Factorial Finder in Rust!");
    println!("Please enter a number: ");

    // Getting input from command line
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("An error occurred while getting user input");

    // We get the result from the calculation and the duration it took
    let loop_result = benchmark(factorial_loop, input.clone());
    let recursion_result = benchmark(factorial_recursion, input.clone());

    // Display results to user
    println!("Factorial of {} is {}!", input.trim(), loop_result.0);
    println!("Using loops it took {} microseconds!", loop_result.1.as_micros());
    println!("Using recursion it took {} microseconds!", recursion_result.1.as_micros());
}

// Function used to benchmark
// This functional only calculates the duration and calls either
// loop or recursion depending on the function we provide it
fn benchmark(f: fn(i64) -> i64, arg: String) -> (i64, Duration) {
    let now = Instant::now();
    let loop_result: i64 = f(arg.trim().parse::<i64>().unwrap());
    return (loop_result, now.elapsed());
}
