(ns pi-approximation-by-throwing-darts)

(defn pi-approx [sampling]
  (letfn [(dart [_]
            (let [x (rand)
                  y (rand)]
              (if (< (+ (Math/pow x 2) (Math/pow y 2)) 1)
                1
                0)))]
    (->> (range sampling)
         (map dart)
         (apply +)
         (#(* (/ % sampling) 4))
         double)))

(let [sampling (if (= (count *command-line-args*) 2)
                 (Integer/parseInt (nth *command-line-args* 1))
                 1000000)]
  (println (str "π ≒ " (pi-approx sampling))))
