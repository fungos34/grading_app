document.addEventListener('DOMContentLoaded', () => {
    const sliders = document.getElementsByClassName("mySlider");
    const participationSlider = document.getElementById("participation");
    const participationSpan = document.getElementById("participationSpan");
    let grade = document.getElementById("grade");
    let examScore = document.getElementById("examScore");
    let participationScore = document.getElementById("participationScore");
    let grading = getGrade();
    grade.innerHTML = grading[0];
    examScore.innerHTML = Math.round(grading[2] * 1000) / 10;
    participationScore.innerHTML = Math.round(grading[3] * 1000) / 10;
    colorizeGrade(grade, grading);

    participationSlider.oninput = function() {
        participationSpan.textContent = `${participationSlider.value} P.`;
        let grading = getGrade();
        grade.innerHTML = grading[0];
        colorizeGrade(grade, grading);
        examScore.innerHTML = Math.round(grading[2] * 1000) / 10;
        participationScore.innerHTML = Math.round(grading[3] * 1000) / 10;
    }

    for (let i = 0; i < sliders.length; i++) {
        const output = document.getElementById(`${i+1}`);
        output.textContent = `${sliders[i].value} P.`;
        sliders[i].oninput = function() {
            output.textContent = `${sliders[i].value} P.`;
            let grading = getGrade();  
            grade.innerHTML = grading[0];          
            colorizeGrade(grade, grading);
            examScore.innerHTML = Math.round(grading[2] * 1000) / 10;
            participationScore.innerHTML = Math.round(grading[3] * 1000) / 10;
        }
    };

    function colorizeGrade(grade, grading) {
        if (grading[0] == 1) {
            grade.style.color = "white";
        } else if (grading[0] == 2) {
            grade.style.color = "yellow";
        } else if (grading[0] == 3) {
            grade.style.color = "orange";
        } else if (grading[0] == 4) {
            grade.style.color = "violet";
        } else {
            grade.style.color = "red";
        }
    }

    function getGrade() {
        // consider participation points weighted 20%
        const participationSlider = document.getElementById("participation");
        let participationPointsRatio = parseFloat(participationSlider.value) / 2;
        let weightedParticipationPointsRatio = participationPointsRatio * 0.2
        // remove worst exam result
        const sliders = document.getElementsByClassName("mySlider");

        let pointsArray = [];
        let sumExamPoints = 0;
        for (let i = 0; i < sliders.length; i++) {
            pointsArray.push(parseFloat(sliders[i].value));
            sumExamPoints += parseFloat(sliders[i].value);
            sliders[i].classList.remove("lowestExamScore");
        }
        let worstExamPoints = Math.min(...pointsArray);
        sumExamPoints -= worstExamPoints;

        for (let i = 0; i < sliders.length; i++) {
            if (sliders[i].value == worstExamPoints) {
                sliders[i].classList.add("lowestExamScore");
                break;
            }
        }

        let examPointsRatio = sumExamPoints / ((pointsArray.length - 1) * 10)
        
        // consider exam points weighted 80%
        let weightedExamPointsRatio = examPointsRatio * 0.8;

        let scorePercentage = (weightedExamPointsRatio + weightedParticipationPointsRatio) * 100;
        // stage the grade according to overall percentage
        let finalGrade = 5;
        if (scorePercentage > 100 - 12.5) {
            finalGrade = 1;
        } else if (scorePercentage > 100 - 25) {
            finalGrade = 2;
        } else if (scorePercentage > 100 - 37.5) {
            finalGrade = 3;
        } else if (scorePercentage > 100 - 50) {
            finalGrade = 4;
        } else {
            finalGrade = 5;
        }

        return [finalGrade, scorePercentage, examPointsRatio, participationPointsRatio];
    }
    
})

