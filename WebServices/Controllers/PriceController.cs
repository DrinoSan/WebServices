using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using WebServices.Models;
using SecuringWebApiUsingApiKey.Attributes;


// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace WebServices.Controllers
{
    [ApiKey]
    [Route("api/[controller]")]
    public class PriceController : Controller
    {
        // Eventually add noise to the increase
        const double increase = 1.2;
        static IDictionary<string, double> currencies = new Dictionary<string, double>() { { "doge", 0.2 }, { "btc", 30000 }, { "eth", 849 } };

        // GET: api/values
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/values/5
        [HttpGet("{id}")]
        public string Get(string id)
        {
            if (id.Equals("all"))
            {
                string allCurrencies = "";
                var keys = new List<string>(currencies.Keys);
                foreach (string key in keys)
                {
                    allCurrencies += "\tName: " + key + " - Current Price: " + currencies[key] + '\n';
                    currencies[key] *= increase;
                }
                return allCurrencies;
            }
            if (!currencies.ContainsKey(id))
                return "We do not support: " + id + ". please try again later";
            currencies[id] *= increase;
            return "Price: " + currencies[id];
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody] CurVal value)
        {
            currencies.Add(value.name, value.value);
        }

        // PUT api/values/5
        [HttpPut]
        public void Put([FromBody] CurVal value)
        {
            currencies[value.name] = value.value;
        }

        // DELETE api/values/5
        [HttpDelete("{key}")]
        public void Delete(string key)
        {
            currencies.Remove(key);
        }
    }
}
