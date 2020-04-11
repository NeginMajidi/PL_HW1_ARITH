load harness

@test "my_test-1" {
  check '1 + 1 * 2' '3'
}

@test "my_test-2" {
  check '-1 + 3 * -2 + 1 * 2 * 0' '-7'
}

@test "my_test-3" {
  check '3 * 2 + 8 * 100 - 6' '800'
}

@test "my_test-4" {
  check '5 * 4 - 3' '17'
}

@test "my_test-5" {
  check '2 * 5 - 3 * 4 + -12' '-14'
}

@test "my_test-6" {
  check '-20 * 2 + 6 * 3 + 5' '-17'
}

@test "my_test-7" {
  check '10 - -10 * 0' '10'
}

@test "my_test-8" {
  check '0 * -0 + 0 - -0' '0'
}

@test "my_test-9" {
  check '2 * 3 * -4 + 3 * 7' '-3'
}

@test "my_test-10" {
  check '-1 + -0 * -7' '-1'
}

@test "my_test-11" {
  check '1 + 2' '3'
}

@test "my_test-12" {
  check '1 + 920' '921'
}

@test "my_test-13" {
  check '1000 + 0' '1000'
}

@test "my_test-14" {
  check '-1 + -5' '-6'
}

@test "my_test-15" {
  check '120 + -30' '90'
}

@test "my_test-16" {
  check '-5 + 0' '-5'
}

@test "my_test-17" {
  check '99 + 30 + 2 + 1' '132'
}

@test "my_test-18" {
  check '2 + 3 + 40 + -1' '44'
}

@test "my_test-19" {
  check '-2 + -6 + 8' '0'
}

@test "my_test-20" {
  check '-2 + -7 + -1' '-10'
}