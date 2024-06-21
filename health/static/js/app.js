const apiUrl = '/api/';

async function createUserProfile() {
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const gender = document.getElementById('gender').value;
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;

    try {
        const response = await fetch(apiUrl + 'user_profiles/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, age, gender, weight, height })
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data);
            showNotification('User created successfully!', 'success');
        } else {
            const errorData = await response.json();
            console.error('Error creating user profile:', errorData);
            showNotification('Failed to create user profile. Please try again.', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showNotification('An error occurred. Please try again.', 'error');
    }
}

async function submitSymptom() {
    const symptom = document.getElementById('symptom').value;

    try {
        const response = await fetch(apiUrl + 'health_data/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ symptom, description: symptom })
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data);
            showNotification('Symptom submitted successfully!', 'success');
        } else {
            const errorData = await response.json();
            console.error('Error submitting symptom:', errorData);
            showNotification('Failed to submit symptom. Please try again.', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showNotification('An error occurred. Please try again.', 'error');
    }
}

async function getHealthPlan() {
    const userId = 1; 

    try {
        const response = await fetch(apiUrl + 'suggest_health_plan/' + userId + '/');

        if (response.ok) {
            const data = await response.json();
            document.getElementById('plans').innerHTML = data.join('<br>');
        } else {
            const errorData = await response.json();
            console.error('Error getting health plan:', errorData);
            showNotification('Failed to get health plan. Please try again.', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showNotification('An error occurred. Please try again.', 'error');
    }
}

function showNotification(message, type) {
    const notification = document.getElementById('notification');
    notification.innerText = message;
    notification.style.color = type === 'success' ? 'green' : 'red';
    notification.style.display = 'block';

    setTimeout(() => {
        notification.style.display = 'none';
    }, 3000);
}
