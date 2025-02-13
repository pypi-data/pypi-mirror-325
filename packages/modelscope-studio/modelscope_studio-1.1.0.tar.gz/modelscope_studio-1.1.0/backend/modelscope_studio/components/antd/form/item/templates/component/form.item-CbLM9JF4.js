import { i as me, a as M, r as pe, g as he, w as k, b as ge } from "./Index-bkv6PIJW.js";
const O = window.ms_globals.React, ae = window.ms_globals.React.forwardRef, ue = window.ms_globals.React.useRef, fe = window.ms_globals.React.useState, de = window.ms_globals.React.useEffect, z = window.ms_globals.React.useMemo, A = window.ms_globals.ReactDOM.createPortal, _e = window.ms_globals.internalContext.useContextPropsContext, V = window.ms_globals.internalContext.ContextPropsProvider, xe = window.ms_globals.internalContext.FormItemContext, be = window.ms_globals.antd.Form, we = window.ms_globals.createItemsContext.createItemsContext;
var Ce = /\s/;
function ye(e) {
  for (var t = e.length; t-- && Ce.test(e.charAt(t)); )
    ;
  return t;
}
var Ee = /^\s+/;
function ve(e) {
  return e && e.slice(0, ye(e) + 1).replace(Ee, "");
}
var B = NaN, Ie = /^[-+]0x[0-9a-f]+$/i, Re = /^0b[01]+$/i, Oe = /^0o[0-7]+$/i, Se = parseInt;
function G(e) {
  if (typeof e == "number")
    return e;
  if (me(e))
    return B;
  if (M(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = M(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = ve(e);
  var s = Re.test(e);
  return s || Oe.test(e) ? Se(e.slice(2), s ? 2 : 8) : Ie.test(e) ? B : +e;
}
var W = function() {
  return pe.Date.now();
}, Fe = "Expected a function", ke = Math.max, Pe = Math.min;
function je(e, t, s) {
  var i, o, n, r, l, a, g = 0, x = !1, c = !1, _ = !0;
  if (typeof e != "function")
    throw new TypeError(Fe);
  t = G(t) || 0, M(s) && (x = !!s.leading, c = "maxWait" in s, n = c ? ke(G(s.maxWait) || 0, t) : n, _ = "trailing" in s ? !!s.trailing : _);
  function f(m) {
    var y = i, F = o;
    return i = o = void 0, g = m, r = e.apply(F, y), r;
  }
  function C(m) {
    return g = m, l = setTimeout(h, t), x ? f(m) : r;
  }
  function d(m) {
    var y = m - a, F = m - g, U = t - y;
    return c ? Pe(U, n - F) : U;
  }
  function p(m) {
    var y = m - a, F = m - g;
    return a === void 0 || y >= t || y < 0 || c && F >= n;
  }
  function h() {
    var m = W();
    if (p(m))
      return b(m);
    l = setTimeout(h, d(m));
  }
  function b(m) {
    return l = void 0, _ && i ? f(m) : (i = o = void 0, r);
  }
  function v() {
    l !== void 0 && clearTimeout(l), g = 0, i = a = o = l = void 0;
  }
  function u() {
    return l === void 0 ? r : b(W());
  }
  function E() {
    var m = W(), y = p(m);
    if (i = arguments, o = this, a = m, y) {
      if (l === void 0)
        return C(a);
      if (c)
        return clearTimeout(l), l = setTimeout(h, t), f(a);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return E.cancel = v, E.flush = u, E;
}
var ne = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Te = O, Le = Symbol.for("react.element"), We = Symbol.for("react.fragment"), Ne = Object.prototype.hasOwnProperty, Ae = Te.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Me = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function re(e, t, s) {
  var i, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Ne.call(t, i) && !Me.hasOwnProperty(i) && (o[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) o[i] === void 0 && (o[i] = t[i]);
  return {
    $$typeof: Le,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: Ae.current
  };
}
L.Fragment = We;
L.jsx = re;
L.jsxs = re;
ne.exports = L;
var w = ne.exports;
const {
  SvelteComponent: De,
  assign: q,
  binding_callbacks: J,
  check_outros: He,
  children: oe,
  claim_element: se,
  claim_space: ze,
  component_subscribe: X,
  compute_slots: Ue,
  create_slot: Ve,
  detach: S,
  element: ie,
  empty: Y,
  exclude_internal_props: K,
  get_all_dirty_from_scope: Be,
  get_slot_changes: Ge,
  group_outros: qe,
  init: Je,
  insert_hydration: P,
  safe_not_equal: Xe,
  set_custom_element_data: le,
  space: Ye,
  transition_in: j,
  transition_out: D,
  update_slot_base: Ke
} = window.__gradio__svelte__internal, {
  beforeUpdate: Qe,
  getContext: Ze,
  onDestroy: $e,
  setContext: et
} = window.__gradio__svelte__internal;
function Q(e) {
  let t, s;
  const i = (
    /*#slots*/
    e[7].default
  ), o = Ve(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ie("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      t = se(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = oe(t);
      o && o.l(r), r.forEach(S), this.h();
    },
    h() {
      le(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      P(n, t, r), o && o.m(t, null), e[9](t), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && Ke(
        o,
        i,
        n,
        /*$$scope*/
        n[6],
        s ? Ge(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Be(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      s || (j(o, n), s = !0);
    },
    o(n) {
      D(o, n), s = !1;
    },
    d(n) {
      n && S(t), o && o.d(n), e[9](null);
    }
  };
}
function tt(e) {
  let t, s, i, o, n = (
    /*$$slots*/
    e[4].default && Q(e)
  );
  return {
    c() {
      t = ie("react-portal-target"), s = Ye(), n && n.c(), i = Y(), this.h();
    },
    l(r) {
      t = se(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), oe(t).forEach(S), s = ze(r), n && n.l(r), i = Y(), this.h();
    },
    h() {
      le(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      P(r, t, l), e[8](t), P(r, s, l), n && n.m(r, l), P(r, i, l), o = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && j(n, 1)) : (n = Q(r), n.c(), j(n, 1), n.m(i.parentNode, i)) : n && (qe(), D(n, 1, 1, () => {
        n = null;
      }), He());
    },
    i(r) {
      o || (j(n), o = !0);
    },
    o(r) {
      D(n), o = !1;
    },
    d(r) {
      r && (S(t), S(s), S(i)), e[8](null), n && n.d(r);
    }
  };
}
function Z(e) {
  const {
    svelteInit: t,
    ...s
  } = e;
  return s;
}
function nt(e, t, s) {
  let i, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Ue(n);
  let {
    svelteInit: a
  } = t;
  const g = k(Z(t)), x = k();
  X(e, x, (u) => s(0, i = u));
  const c = k();
  X(e, c, (u) => s(1, o = u));
  const _ = [], f = Ze("$$ms-gr-react-wrapper"), {
    slotKey: C,
    slotIndex: d,
    subSlotIndex: p
  } = he() || {}, h = a({
    parent: f,
    props: g,
    target: x,
    slot: c,
    slotKey: C,
    slotIndex: d,
    subSlotIndex: p,
    onDestroy(u) {
      _.push(u);
    }
  });
  et("$$ms-gr-react-wrapper", h), Qe(() => {
    g.set(Z(t));
  }), $e(() => {
    _.forEach((u) => u());
  });
  function b(u) {
    J[u ? "unshift" : "push"](() => {
      i = u, x.set(i);
    });
  }
  function v(u) {
    J[u ? "unshift" : "push"](() => {
      o = u, c.set(o);
    });
  }
  return e.$$set = (u) => {
    s(17, t = q(q({}, t), K(u))), "svelteInit" in u && s(5, a = u.svelteInit), "$$scope" in u && s(6, r = u.$$scope);
  }, t = K(t), [i, o, x, c, l, a, r, n, b, v];
}
class rt extends De {
  constructor(t) {
    super(), Je(this, t, nt, tt, Xe, {
      svelteInit: 5
    });
  }
}
const $ = window.ms_globals.rerender, N = window.ms_globals.tree;
function ot(e, t = {}) {
  function s(i) {
    const o = k(), n = new rt({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? N;
          return a.nodes = [...a.nodes, l], $({
            createPortal: A,
            node: N
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((g) => g.svelteInstance !== o), $({
              createPortal: A,
              node: N
            });
          }), l;
        },
        ...i.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(s);
    });
  });
}
const st = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function it(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const i = e[s];
    return t[s] = lt(s, i), t;
  }, {}) : {};
}
function lt(e, t) {
  return typeof t == "number" && !st.includes(e) ? t + "px" : t;
}
function H(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const o = O.Children.toArray(e._reactElement.props.children).map((n) => {
      if (O.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = H(n.props.el);
        return O.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...O.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(A(O.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: o
    }), s)), {
      clonedElement: s,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: r,
      type: l,
      useCapture: a
    }) => {
      s.addEventListener(l, r, a);
    });
  });
  const i = Array.from(e.childNodes);
  for (let o = 0; o < i.length; o++) {
    const n = i[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = H(n);
      t.push(...l), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: t
  };
}
function ct(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const I = ae(({
  slot: e,
  clone: t,
  className: s,
  style: i,
  observeAttributes: o
}, n) => {
  const r = ue(), [l, a] = fe([]), {
    forceClone: g
  } = _e(), x = g ? !0 : t;
  return de(() => {
    var C;
    if (!r.current || !e)
      return;
    let c = e;
    function _() {
      let d = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (d = c.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), ct(n, d), s && d.classList.add(...s.split(" ")), i) {
        const p = it(i);
        Object.keys(p).forEach((h) => {
          d.style[h] = p[h];
        });
      }
    }
    let f = null;
    if (x && window.MutationObserver) {
      let d = function() {
        var v, u, E;
        (v = r.current) != null && v.contains(c) && ((u = r.current) == null || u.removeChild(c));
        const {
          portals: h,
          clonedElement: b
        } = H(e);
        c = b, a(h), c.style.display = "contents", _(), (E = r.current) == null || E.appendChild(c);
      };
      d();
      const p = je(() => {
        d(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      f = new window.MutationObserver(p), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", _(), (C = r.current) == null || C.appendChild(c);
    return () => {
      var d, p;
      c.style.display = "", (d = r.current) != null && d.contains(c) && ((p = r.current) == null || p.removeChild(c)), f == null || f.disconnect();
    };
  }, [e, x, s, i, n, o]), O.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function at(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function T(e, t = !1) {
  try {
    if (ge(e))
      return e;
    if (t && !at(e))
      return;
    if (typeof e == "string") {
      let s = e.trim();
      return s.startsWith(";") && (s = s.slice(1)), s.endsWith(";") && (s = s.slice(0, -1)), new Function(`return (...args) => (${s})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function R(e, t) {
  return z(() => T(e, t), [e, t]);
}
function ce(e, t, s) {
  const i = e.filter(Boolean);
  if (i.length !== 0)
    return i.map((o, n) => {
      var g;
      if (typeof o != "object")
        return o;
      const r = {
        ...o.props,
        key: ((g = o.props) == null ? void 0 : g.key) ?? (s ? `${s}-${n}` : `${n}`)
      };
      let l = r;
      Object.keys(o.slots).forEach((x) => {
        if (!o.slots[x] || !(o.slots[x] instanceof Element) && !o.slots[x].el)
          return;
        const c = x.split(".");
        c.forEach((h, b) => {
          l[h] || (l[h] = {}), b !== c.length - 1 && (l = r[h]);
        });
        const _ = o.slots[x];
        let f, C, d = !1, p = t == null ? void 0 : t.forceClone;
        _ instanceof Element ? f = _ : (f = _.el, C = _.callback, d = _.clone ?? d, p = _.forceClone ?? p), p = p ?? !!C, l[c[c.length - 1]] = f ? C ? (...h) => (C(c[c.length - 1], h), /* @__PURE__ */ w.jsx(V, {
          params: h,
          forceClone: p,
          children: /* @__PURE__ */ w.jsx(I, {
            slot: f,
            clone: d
          })
        })) : /* @__PURE__ */ w.jsx(V, {
          forceClone: p,
          children: /* @__PURE__ */ w.jsx(I, {
            slot: f,
            clone: d
          })
        }) : l[c[c.length - 1]], l = r;
      });
      const a = "children";
      return o[a] && (r[a] = ce(o[a], t, `${n}`)), r;
    });
}
const {
  withItemsContextProvider: ut,
  useItems: ft,
  ItemHandler: pt
} = we("antd-form-item-rules");
function dt(e) {
  const t = e.pattern;
  return {
    ...e,
    pattern: (() => {
      if (typeof t == "string" && t.startsWith("/")) {
        const s = t.match(/^\/(.+)\/([gimuy]*)$/);
        if (s) {
          const [, i, o] = s;
          return new RegExp(i, o);
        }
      }
      return typeof t == "string" ? new RegExp(t) : void 0;
    })() ? new RegExp(t) : void 0,
    defaultField: T(e.defaultField) || e.defaultField,
    transform: T(e.transform),
    validator: T(e.validator)
  };
}
function ee(e) {
  return typeof e == "object" && e !== null ? e : {};
}
const te = ({
  children: e,
  ...t
}) => /* @__PURE__ */ w.jsx(xe.Provider, {
  value: z(() => t, [t]),
  children: e
}), ht = ot(ut(["rules"], ({
  slots: e,
  getValueFromEvent: t,
  getValueProps: s,
  normalize: i,
  shouldUpdate: o,
  tooltip: n,
  rules: r,
  children: l,
  hasFeedback: a,
  ...g
}) => {
  const x = e["tooltip.icon"] || e["tooltip.title"] || typeof n == "object", c = typeof a == "object", _ = ee(a), f = R(_.icons), C = R(t), d = R(s), p = R(i), h = R(o), b = ee(n), v = R(b.afterOpenChange), u = R(b.getPopupContainer), {
    items: {
      rules: E
    }
  } = ft();
  return /* @__PURE__ */ w.jsx(be.Item, {
    ...g,
    hasFeedback: c ? {
      ..._,
      icons: f || _.icons
    } : a,
    getValueFromEvent: C,
    getValueProps: d,
    normalize: p,
    shouldUpdate: h || o,
    rules: z(() => {
      var m;
      return (m = r || ce(E)) == null ? void 0 : m.map((y) => dt(y));
    }, [E, r]),
    tooltip: e.tooltip ? /* @__PURE__ */ w.jsx(I, {
      slot: e.tooltip
    }) : x ? {
      ...b,
      afterOpenChange: v,
      getPopupContainer: u,
      icon: e["tooltip.icon"] ? /* @__PURE__ */ w.jsx(I, {
        slot: e["tooltip.icon"]
      }) : b.icon,
      title: e["tooltip.title"] ? /* @__PURE__ */ w.jsx(I, {
        slot: e["tooltip.title"]
      }) : b.title
    } : n,
    extra: e.extra ? /* @__PURE__ */ w.jsx(I, {
      slot: e.extra
    }) : g.extra,
    help: e.help ? /* @__PURE__ */ w.jsx(I, {
      slot: e.help
    }) : g.help,
    label: e.label ? /* @__PURE__ */ w.jsx(I, {
      slot: e.label
    }) : g.label,
    children: h || o ? () => /* @__PURE__ */ w.jsx(te, {
      children: l
    }) : /* @__PURE__ */ w.jsx(te, {
      children: l
    })
  });
}));
export {
  ht as FormItem,
  ht as default
};
