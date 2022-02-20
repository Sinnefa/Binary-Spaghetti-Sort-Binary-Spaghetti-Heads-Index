BinarySpaghettiSort <- function(values, reverse=F) {
  length <- length(values)
  sorted <- c()
  maximum <- max(values)
  minimum <- min(values)
  binary_spaghetti_heads_index <- rep(0, (maximum-minimum+1))
  
  for (i in seq_along(values)) {
    n = values[[i]]
    position <- (n-minimum+1)
    binary_spaghetti_heads_index[position] <- binary_spaghetti_heads_index[position] + bitwShiftL(1,(length-i))
  }
  index <- 1
  start <- 1
  stop <- length(binary_spaghetti_heads_index)
  pace <- 1
  if (reverse==T) {
    start <- length(binary_spaghetti_heads_index)
    stop <- 1
    pace <- -1
  }
  for (i in seq(start,stop,pace)) {
    vxor <- binary_spaghetti_heads_index[i]
    while (vxor > 0) {
      k <- round(log2(vxor), digits = 0)
      sorted[index] <- values[length-k]
      vxor <- bitwXor(vxor, bitwShiftL(1,k))
      index <- index + 1
    }
  }
  return <- sorted
}
